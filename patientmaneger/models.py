from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    reType = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    UniqueId = models.CharField(max_length=255)
    dob = models.CharField(max_length=15)



# Create your models here.
