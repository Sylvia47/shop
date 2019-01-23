from django.db import models
from items.models import Product

class Orderlist(models.Model):
    item = models.ManyToManyField(Product)
    amount = models.PositiveIntegerField(blank = False)
        
    
    def __int__(self):
        return self.id
# Create your models here.
