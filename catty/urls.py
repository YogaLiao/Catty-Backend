from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('ok/', views.ok_view),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('services/', views.ServiceList.as_view(), name = 'service_list'),
    path('services/<int:pk>', views.ServiceDetail.as_view(), name = 'service_detail')
]

