from django.urls import path
from . import views

urlpatterns = [
    path('ok/', views.ok_view),
    path('users/', views.UserList.as_view()),
    path('services/', views.ServiceList.as_view()),
    path('services/<int:pk>', views.ServiceDetail.as_view())
]

