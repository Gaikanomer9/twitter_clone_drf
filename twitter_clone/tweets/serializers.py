# tweets/serializers.py
from rest_framework import serializers
from .models import Tweet

class TweetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']

    def create(self, validated_data):
        user = self.context['request'].user
        tweet = Tweet.objects.create(author=user, **validated_data)
        return tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'author', 'content', 'created_at']