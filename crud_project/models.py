from django.db import models


# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=64)
    lastname= models.CharField(max_length=15)
