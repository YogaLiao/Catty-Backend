from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import ReviewSerializer, UserInfoSerializer, ServiceSerializer
from .models import Review, UserInfo, Service
from django_filters.rest_framework import DjangoFilterBackend



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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ServiceSearchList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['service','zipcode','rate','username']

class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        print(request.data)
        print(request.user.username)
        request.user.id = request.data['written_to']
        return super().post(request, *args, **kwargs)






# class TweetListProtected(generics.ListCreateAPIView):
#     serializer_class = TweetSerializer
#     queryset = Tweet.objects.all()

#     permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]






# Create your views here.
