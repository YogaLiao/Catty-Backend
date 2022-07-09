from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model


# Create your views here.

def ok_view(request):
    return HttpResponse("ok!")

    
# class TweetList(generics.ListCreateAPIView):
#     serializer_class = TweetSerializer
#     queryset = Tweet.objects.all()
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def post(self, request, *args, **kwargs):
#         print(request.user.username)
#         request.data['user_string'] = request.user.username
#         return super().post(request, *args, **kwargs)

# class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TweetSerializer
#     queryset = Tweet.objects.all()

# class TweetListProtected(generics.ListCreateAPIView):
#     serializer_class = TweetSerializer
#     queryset = Tweet.objects.all()

#     permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]






# Create your views here.
