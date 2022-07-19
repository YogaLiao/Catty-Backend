from rest_framework import serializers
from .models import Review, UserInfo, Service
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id','written_by','written_to','date','content','rating')

class ServiceSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(read_only = True, many=True)
    # username = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only = True
    # )
    zipcode = serializers.ReadOnlyField(source='user.zipcode')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    address = serializers.ReadOnlyField(source='user.address')
    city = serializers.ReadOnlyField(source='user.city')
    state = serializers.ReadOnlyField(source='user.state')
    cell = serializers.ReadOnlyField(source='user.cell')
    url = serializers.ReadOnlyField(source='user.url')
    username = serializers.ReadOnlyField(source = 'user.username')
    about = serializers.ReadOnlyField(source = 'user.about')

    class Meta:
        model = Service
        fields = ('id','user','displayName', 'headline', 'service', 'rate', 'note', 'disable','zipcode','first_name','last_name','address','city','state','cell', 'url', 'username', 'about', 'reviews')

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