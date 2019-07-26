from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserViewSet(APIView):
    def get(self, request):
        serializer_class = serializers.UserSerializer(request.user)
        return Response(serializer_class.data)

    def post(self, request):
        serializer_class = serializers.UserSerializer(data=request.data)
        if serializer_class.is_valid():
            user = serializer_class.save()
            user.set_password(request.data['password1'])
            user.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
