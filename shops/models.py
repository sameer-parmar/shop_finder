from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    latitude= models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]

    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )

    def __str__(self):
        return self.name