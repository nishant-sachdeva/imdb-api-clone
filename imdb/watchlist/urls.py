from django.urls import path, include
from watchlist.views import movie_list, movie_detail

urlpatterns = [
    path('list/', movie_list, name='movie_list'),
    path('<int:pk>', movie_detail, name='movie_detail'),
]
