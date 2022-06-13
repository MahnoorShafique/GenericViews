from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


class UserCreateApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteApi(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer