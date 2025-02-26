from django.db import models

from core.models import BaseModel
from django.db import models

class Item(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    category = models.ForeignKey('Category', related_name='items', on_delete=models.CASCADE)
    stock_qty = models.PositiveIntegerField()
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=2006)

    def __str__(self):
        return self.name