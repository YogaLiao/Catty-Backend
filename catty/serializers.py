from rest_framework import serializers
from .models import UserInfo, Service


class ServiceSerializer(serializers.ModelSerializer):
    # username = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only = True
    # )
    
    class Meta:
        model = Service
        fields = ('id','user','displayName', 'headline', 'service', 'rate', 'note', 'disable')

class UserInfoSerializer(serializers.ModelSerializer):
    services = ServiceSerializer (read_only = True, many=True)

    class Meta:
        model = UserInfo
        fields = ('id','username', 'first_name', 'last_name', 'dob_month', 'dob_day',
        'dob_year', 'address', 'city', 'state', 'zipcode', 'cell','url', 'about', 'biSitter', 'services')
    
    # def create(self, validated_data):
    #     services_data = validated_data.pop('services')
    #     user = UserInfo.objects.create(**validated_data)
    #     for service_data in services_data:
    #         Service.objects.create(user=user, **service_data)
    #     return user