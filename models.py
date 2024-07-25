from django.db import models
from django.contrib.auth.models import User


class book (models.Model):
    title =models.CharField(max_length=200)
    Author = models.CharField(max_length=100)
    published_date =models.DateField()
    price =models.DecimalField(max_digits=6,decimal_places=2)

  
    def __str__(self):
        return self.title

