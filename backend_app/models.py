from django.db import models

class RegisterUser(models.Model):
    email = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
