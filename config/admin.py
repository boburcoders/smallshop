from django.contrib import admin

from config.models import Seller, Product, Category

# Register your models here.


admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Category)
