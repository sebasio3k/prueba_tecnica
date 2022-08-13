from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from users.models import Users
from users.serializers.v1.users_serializers import UserSerializer


class ListUsers(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
