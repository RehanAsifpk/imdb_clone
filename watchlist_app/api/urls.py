from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list , movie_details
from watchlist_app.api.views import WatchListAV , WatchDetailAV, StreamPlatformAV,StreamPlatformDetailAV,ReviewList,ReviewDetail, ReviewCreate,StreamPlatformViewSet

router=DefaultRouter()
router.register('stream',StreamPlatformViewSet, basename='streamplatform')

urlpatterns = [
    # path("list/",movie_list,name='movie-list'),
    # path('<int:pk>',movie_details, name='movie-details')
    path("list/",WatchListAV.as_view(),name='watch-list'),
    path('list/<int:pk>',WatchDetailAV.as_view(), name='watch-details'),
    
    path('',include(router.urls)),
    
    # path("stream/",StreamPlatformAV.as_view(),name='stream'),
    # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    # path('review',ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(), name='review-detail'),
    
    path('list/<int:pk>/review-create',ReviewCreate.as_view(), name='review-create'),
    path('list/<int:pk>/review',ReviewList.as_view(), name='review-list'),
    path('list/review/<int:pk>',ReviewDetail.as_view(), name='review-detail')
    
]
