from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar', 'mobile', 'date_of_birth', 'gender')


class UserSerializer(serializers.ModelSerializer):
    friends = FriendsSerializer(many=True, read_only=True)
    avatar = serializers.URLField(read_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar', 'mobile', 'gender', 'date_of_birth', 'friends')


