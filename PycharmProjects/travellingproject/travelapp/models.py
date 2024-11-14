from django.db import models

# Create your models here.



class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class User(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)




