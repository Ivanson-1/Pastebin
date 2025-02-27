from django.db import models


class TextBlock(models.Model):
    text = models.TextField()
    link = models.CharField()
    time = models.DateTimeField()
