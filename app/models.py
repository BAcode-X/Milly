from django.conf import settings
from django.utils.translation import gettext as _
from django.db import models


# Create your models here.
class Cloth(models.Model):
    types = (
        ('Shirts','Shirts'),
        ('Dresses', 'Dresses'),
        ('Jeans', 'Jeans'),
        ('Jackets', 'Jackets'),
        ('Gymwear', 'Gymwear'),
        ('Shoes', 'Shoes')
    )
    text = models.CharField(max_length=200)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')
    tag = models.CharField(max_length=10, choices=types, default='Jeans')

    def __str__(self):
        return self.text
    