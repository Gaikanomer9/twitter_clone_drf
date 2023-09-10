from django.urls import include, path
from users.views import FollowView, FollowListView, UserListView

urlpatterns = [
    path('', include('djoser.urls')),
    path('users/<int:id>/follow/', FollowView.as_view()),
    path('following/', FollowListView.as_view()),
    path('users/', UserListView.as_view()),
    path('auth/', include('djoser.urls.authtoken')),
]