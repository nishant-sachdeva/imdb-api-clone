from django.urls import path, include
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import WatchListAV, WatchListDetailAV
from watchlist.api.views import StreamPlatformAV, StreamPlatformDetailAV
from watchlist.api.views import ReviewList, ReviewDetail 

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('list/<int:pk>', WatchListDetailAV.as_view(), name='watch_list_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream_platform'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_platform_detail'),
    path('review/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
]
