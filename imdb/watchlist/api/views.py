from rest_framework.response  import Response

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView 
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins

from watchlist.models import WatchList, StreamPlatform, Review
from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
 
from rest_framework import status

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


from watchlist.api.permissions import IsAdminOrReadOnly, IsReviewUserorReadOnly

from watchlist.api.throttling import ReviewCreateThrottle, ReviewListThrottle
from rest_framework.throttling import UserRateThrottle, AnonCreateThrottle, ScopeRateThrottle


class UserReview(generics.ListAPIView):
	serializer_class = ReviewSerializer
	# throttle_classes = [ReviewListThrottle, AnonRateThrottle]

	def get_queryset(self):
		pk = self.kwargs['username']
		return Review.objects.filter(review_user=pk)



class ReviewCreate(generics.CreateAPIView):
	permission_classes = [IsAuthenticated]

	# we need to overwrite the current function
	serializer_class = ReviewSerializer

	def get_queryset(self):
		return Review.objects.all()

	def perform_create(self, serializer):
		pk = self.kwargs.get('pk')
		watchlist = WatchList.objects.get(pk=pk)
		# watchlist = get_object_or_404(queryset, pk=pk)

		review_user = self.request.user 
		review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

		if review_queryset.exists():
			raise ValidationError("Can't comment on same movie more than once!")

		if watchlist.number_of_rating == 0:
			watchlist.avg_rating = serializer.validated_data['rating']
		else:
			watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2

		watchlist.number_of_rating = watchlist.number_of_rating + 1
		watchlist.save()

		serializer.save(watchlist=watchlist, review_user=review_user)

class ReviewList(generics.ListCreateAPIView):
	throttle_classes = [UserRateThrottle, AnonRateThrottle]
	# queryset = Review.objects.all()
	serializer_class = ReviewSerializer
	# permission_classes = [IsAuthenticated]
	# no need for permissions here,since we anyone can see list


	# here, we overwrite queryset
	def get_queryset(self):
		pk = self.kwargs['pk']
		return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
	throttle_classes = [UserRateThrottle, AnonRateThrottle]

	permission_classes = [IsReviewUserorReadOnly]

	queryset = Review.objects.all()
	serializer_class = ReviewSerializer


class StreamPlatformViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminOrReadOnly]

	queryset = StreamPlatform.objects.all()
	serializer_class = StreamPlatformSerializer


# class StreamPlatformViewSet(viewsets.ViewSet):
	
# 	def list(self, request):
# 		queryset = StreamPlatform.objects.all()
# 		serializer = StreamPlatformSerializer(queryset, many=True)
# 		return Response(serializer.data)

# 	def retrieve(self, request, pk=None):
# 		queryset = StreamPlatform.objects.all()
# 		watchlist = get_object_or_404(queryset, pk=pk)
# 		serializer = StreamPlatformSerializer(watchlist)
# 		return Response(serializer.data)

# 	def create(self, request):
# 		serializer = StreamPlatformSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		else:
# 			return Response(serializer.errors)


class StreamPlatformAV(APIView):
	permission_classes = [IsAdminOrReadOnly]

	def get(self, request):
		platforms = StreamPlatform.objects.all()
		serializer = StreamPlatformSerializer(platforms, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = StreamPlatformSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
	permission_classes = [IsAdminOrReadOnly]

	def get(self, request, pk):
		try:
			platform = StreamPlatform.objects.get(pk=pk)
		except StreamPlatform.DoesNotExist:
			return Response({'Detail' : 'Not Found'}, status = status.HTTP_404_NOT_FOUND)
		serializer = StreamPlatformSerializer(platform)
		return Response(serializer.data)

	def put(self, request, pk):
		platform = StreamPlatform.objects.get(pk=pk)
		serializer = StreamPlatformSerializer(platform, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_404_BAD_CONTENT)

	def delete(self, request, pk):
		platform = StreamPlatform.objects.get(pk=pk)
		platform.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):
	permission_classes = [IsAdminOrReadOnly]
	def get(self,request):
		movies = WatchList.objects.all()
		serializer = WatchListSerializer(movies, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = WatchListSerializer(data = request.data)
		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class WatchListDetailAV(APIView):
	permission_classes = [IsAdminOrReadOnly]
	def get(self, request, pk):
		try:
			mov_obj = WatchList.objects.get(pk = pk)
		except WatchList.DoesNotExist:
			return Response({'Detail' : 'Not found'}, status = status.HTTP_404_NOT_FOUND)

		serializer = WatchListSerializer(mov_obj)
		return Response(serializer.data)

	def put(self, request, pk):
		mov_obj = WatchList.objects.get(pk = pk)

		serializer = WatchListSerializer(mov_obj, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_404_BAD_CONTENT)

	def delete(self, request, pk):
		mov_obj = WatchList.objects.get(pk = pk)
		mov_obj.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)