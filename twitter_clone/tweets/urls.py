from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tweets.views import TweetViewSet, TweetListFeed

router = DefaultRouter()
router.register('tweets', TweetViewSet, basename='tweets')


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', TweetListFeed.as_view()),
]