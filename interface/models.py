from django.db import models


class Image(models.Model):
    username = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')
