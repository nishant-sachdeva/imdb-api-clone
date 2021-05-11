from django.urls import path, include
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import WatchListAV, WatchListDetailAV
from watchlist.api.views import StreamPlatformAV, StreamPlatformDetailAV
from watchlist.api.views import ReviewList, ReviewDetail ,ReviewCreate
from watchlist.api.views import StreamPlatformViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='streamplatform')



urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='watch_list_detail'),
    
    path('', include(router.urls)),

    # path('stream/', StreamPlatformViewSet.as_view({'get':'list'}), name='stream_platform'),
    # path('stream/<int:pk>', StreamPlatformViewSet.as_view({'get':'retrieve'}), name='stream_platform_detail'),
    
    # path('review/', ReviewList.as_view(), name='review_list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review_create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),


]
