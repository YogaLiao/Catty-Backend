from rest_framework import serializers
from .models import UserInfo, Service

class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('uuid', 'username', 'email', 'first_name', 'last_name', 'dob_month', 'dob_day',
        'dob_year', 'address', 'city', 'state', 'zipcode', 'url', 'about', 'biSitter')

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('username','displayName', 'headline', 'service', 'rate', 'note', 'disable')