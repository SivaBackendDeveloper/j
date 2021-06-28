import os

from django.db import models
# Create your models here.


class Member(models.Model):
 name=models.CharField(max_length=100)
 role=models.CharField(max_length=100)
 area=models.CharField(max_length=100)
 mobilenumber=models.BigIntegerField()
