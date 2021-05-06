from django.urls import path, include
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import WatchListAV, WatchListDetailAV
from watchlist.api.views import StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('list/<int:pk>', WatchListDetailAV.as_view(), name='watch_list_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream_platform'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_platform_detail'),

]
