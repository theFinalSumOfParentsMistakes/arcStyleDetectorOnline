from django.db import models


class myImage(models.Model):
    image = models.ImageField(upload_to='images')
