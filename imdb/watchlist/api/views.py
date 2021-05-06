from rest_framework.response  import Response
from rest_framework.views import APIView 
from watchlist.models import WatchList, StreamPlatform, Review
from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
 
from rest_framework import status

class ReviewAV(APIView):
	def get(self, request):
		reviews = Review.objects.all()
		serializer = ReviewSerializer(reviews, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ReviewSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

class ReviewDetailAV(APIView):
	def get(self, request, pk):
		try:
			review = Review.objects.get(pk=pk)
		except Review.DoesNotExist:
			return Response({'Error' : 'Not Found'}, status = status.HTTP_404_NOT_FOUND)
		serializer = ReviewSerializer(review)
		return Response(serializer.data)

	def put(self, request, pk):
		review = Review.objects.get(pk=pk)
		serializer =  ReviewSerializer(review, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_404_BAD_CONTENT)

	def delete(self, request, pk):
		review = Review.objects.get(pk=pk)
		review.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformAV(APIView):
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
	def get(self, request, pk):
		try:
			platform = StreamPlatform.objects.get(pk=pk)
		except StreamPlatform.DoesNotExist:
			return Response({'Error' : 'Not Found'}, status = status.HTTP_404_NOT_FOUND)
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
	def get(self, request, pk):
		try:
			mov_obj = WatchList.objects.get(pk = pk)
		except WatchList.DoesNotExist:
			return Response({'Error' : 'Not found'}, status = status.HTTP_404_NOT_FOUND)

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