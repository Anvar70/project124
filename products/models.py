from django.db import models

# Create your models here.
class ProductsModel(models.Model):
    name = models.CharField(max_length=77)
    description = models.TextField()
    price = models.PositiveIntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
