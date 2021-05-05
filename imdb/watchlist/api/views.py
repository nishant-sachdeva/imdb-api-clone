from rest_framework.response  import Response
from rest_framework.decorators import api_view
from watchlist.models import movie
from watchlist.api.serializers import movieSerializer


@api_view()
def movie_list(request):
	movie_list = movie.objects.all()
	# print(list(movies.values))

	serializer = movieSerializer(movie_list, many=True)
	# this "many" is the attribute that tells it that multiple
	# objects are coming

	return Response(serializer.data) 

@api_view()
def movie_detail(request, pk):
	# no code here yet
	mov_obj = movie.objects.get(pk = pk)
	serializer = movieSerializer(mov_obj)
	return Response(serializer.data)

