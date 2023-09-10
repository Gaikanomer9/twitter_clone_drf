from rest_framework import serializers

from users.models import  User


class ProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email', 'username', 'first_name',
            'last_name', 'id'
        )
