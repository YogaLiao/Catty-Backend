from rest_framework import serializers
from .models import UserInfo, Service

class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    services = serializers.HyperlinkedRelatedField(
        view_name = 'service_detail',
        many=True,
        read_only = True
    )

    class Meta:
        model = UserInfo
        fields = ('uuid', 'username', 'first_name', 'last_name', 'dob_month', 'dob_day',
        'dob_year', 'address', 'city', 'state', 'zipcode', 'cell','url', 'about', 'biSitter', 'services')

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only = True
    )
    class Meta:
        model = Service
        fields = ('username','displayName', 'headline', 'service', 'rate', 'note', 'disable')