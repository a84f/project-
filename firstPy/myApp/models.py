from django.db import models

# Create your models here.
class Contactt(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    message = models.CharField(max_length=300)

class Users(models.Model):
        username = models.CharField(max_length=120)
        password = models.CharField(max_length=120)
