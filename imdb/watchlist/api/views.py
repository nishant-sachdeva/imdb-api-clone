from rest_framework.response  import Response

from rest_framework.views import APIView 
from rest_framework import generics
from rest_framework import mixins

from watchlist.models import WatchList, StreamPlatform, Review
from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
 
from rest_framework import status


class ReviewList(generics.ListCreateAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer


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