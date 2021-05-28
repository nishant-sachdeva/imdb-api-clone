from django.urls import path, include
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import WatchListAV, WatchListDetailAV
from watchlist.api.views import StreamPlatformAV, StreamPlatformDetailAV
from watchlist.api.views import ReviewList, ReviewDetail ,ReviewCreate
from watchlist.api.views import StreamPlatformViewSet, UserReview, WatchListGV

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='streamplatform')



urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='watch_list_detail'),
    path('new_list/', WatchListGV.as_view(), name='watch_list2'),
    
    path('', include(router.urls)),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review_create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),

    path('reviews/', UserReview.as_view(), name='user-review_detail')
]
