from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserInfoSerializer, ServiceSerializer
from .models import UserInfo, Service


# Create your views here.

def ok_view(request):
    return HttpResponse("ok!")

    
class UserList(generics.ListCreateAPIView):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        print(request.user.username)
        request.data['username'] = request.user.username
        return super().post(request, *args, **kwargs)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    
class ServiceList(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        print("request.user.username")
        print(request.user.id)
        print(request.user.pk)
        # request.data['username'] = request.user.id
        request.data['user'] = request.user.id - 1
        return super().post(request, *args, **kwargs)

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

# class TweetListProtected(generics.ListCreateAPIView):
#     serializer_class = TweetSerializer
#     queryset = Tweet.objects.all()

#     permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]






# Create your views here.
