from django.contrib.postgres.fields import ArrayField
from django.db import models
import uuid


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=100, default='unknown_user')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    dob_month = models.CharField(max_length=100, default='')
    dob_day = models.CharField(max_length=100, default='')
    dob_year = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    zipcode = models.CharField(max_length=5, default='')
    cell = models.CharField(max_length=10,default='')
    url = models.CharField(max_length=500)
    about = models.CharField(max_length=256, default='')
    biSitter = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Service(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name= 'services')
    displayName = models.CharField(max_length=100, default=user)
    headline = models.CharField(max_length=100, default='')
    service = models.CharField(max_length=100, default='onboarding')
    rate = models.IntegerField()
    note = models.CharField(max_length=100, default='', blank = True)
    disable = ArrayField(models.CharField(max_length=20, blank = True))

    def __str__(self):
        return self.service