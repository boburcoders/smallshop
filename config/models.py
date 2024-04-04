from django.db import models
import os


class Seller(models.Model):
    name = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=25, null=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='seller/logos/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=30)
    count_product = models.IntegerField(default=0)
    price = models.FloatField()
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='product/images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
