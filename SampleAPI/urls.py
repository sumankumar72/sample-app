from django.urls import path, include
from rest_framework import routers
from . import viewsets

# router = routers.DefaultRouter()
# router.register(r'', viewsets.UserViewSet)

urlpatterns = [
    path('me', viewsets.UserViewSet.as_view(), name='user_profile'),
    path('user/register', viewsets.UserViewSet.as_view(), name='register_user'),
]