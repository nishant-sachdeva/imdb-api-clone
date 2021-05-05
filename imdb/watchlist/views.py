from django.shortcuts import render
from watchlist.models import movie

from django.http import JsonResponse

def movie_list(request):
	# first we get all the movis
	movies = movie.objects.all()
	# we cannot return directly, we need to return json
	# convert the query set into a python dict

	data = {
		'movies' : list(movies.values())
	}
	return JsonResponse(data)



def movie_detail(request, pk):
	# pk is the primary key of the movie that we want
	movie_obj = movie.objects.get(pk=pk)

	data = {
	'name': movie_obj.name, 
	'desc' : movie_obj.about,
	'active': movie_obj.active,
	}

	return JsonResponse(data)