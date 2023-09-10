# tweets/views.py
from rest_framework import generics
from .models import Tweet
from .serializers import TweetCreateSerializer, TweetSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)


from tweets.permissions import IsAuthorOrReadOnly

# class TweetListCreateView(generics.ListCreateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetCreateSerializer
#     permission_classes = [IsAuthenticated]

# class TweetDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#     permission_classes = [IsAuthenticated]

class TweetViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Tweet.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TweetSerializer
        return TweetCreateSerializer
    
    
class TweetListFeed(generics.ListAPIView):
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Tweet.objects.filter(author__in=self.request.user.following.all())
        