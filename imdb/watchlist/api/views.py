from rest_framework.response  import Response
from rest_framework.decorators import api_view
from watchlist.models import movie
from watchlist.api.serializers import movieSerializer

from rest_framework import status


@api_view(['GET', 'POST'])
def movie_list(request):
	if request.method == 'GET':
		movie_list = movie.objects.all()
		serializer = movieSerializer(movie_list, many=True)
		return Response(serializer.data) 
	if request.method == 'POST':
		serializer = movieSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
	# no code here yet'
	if request.method == 'GET':
		try:
			mov_obj = movie.objects.get(pk = pk)
		except movie.DoesNotExist:
			return Response({'Error' : 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
		
		serializer = movieSerializer(mov_obj)
		return Response(serializer.data)

	if request.method == 'PUT':
		mov_obj = movie.objects.get(pk = pk)

		serializer = movieSerializer(mov_obj, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_404_BAD_CONTENT)

	if request.method == 'DELETE':
		mov_obj = movie.objects.get(pk = pk)
		mov_obj.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


