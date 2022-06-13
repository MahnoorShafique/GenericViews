from django.urls import path

from user.views import UserCreateApi, UserApi, UserUpdateApi, UserDeleteApi

urlpatterns = [
    path('create',UserCreateApi.as_view()),
    path('list', UserApi.as_view()),
    path('update/<int:pk>',UserUpdateApi.as_view()),
    path('api/<int:pk>/de', UserDeleteApi.as_view()),
    ]