from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class can1(models.Model):
    water=models.CharField(max_length=100)
    cwater=models.CharField(max_length=100)
    

    