from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def clean(self):
        if self.price < 0:
            raise ValidationError('Price cannot be negative')
        if self.inventory < 0:
            raise ValidationError('Inventory cannot be negative')
