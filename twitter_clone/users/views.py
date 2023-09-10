from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import ProfileSerializers

from users.models import User

# Create your views here.

class FollowView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id):
        user = get_object_or_404(User, pk=id)
        request.user.following.add(user)
        return Response(status=204)
    
    def delete(self, request, id):
        user = get_object_or_404(User, pk=id)
        request.user.following.remove(user)
        return Response(status=204)
    
class FollowListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        users = request.user.following.all()
        serializer = ProfileSerializers(users, many=True)
        return Response(serializer.data)
    
class UserListView(APIView):
    permission_classes = []
    
    def get(self, request):
        users = User.objects.all()
        serializer = ProfileSerializers(users, many=True)
        return Response(serializer.data)