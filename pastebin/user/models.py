from django.db import models


class User(models.Model):
    name = models.CharField()
    login = models.CharField(unique=True)
    password = models.CharField()

