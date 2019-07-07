from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2048)