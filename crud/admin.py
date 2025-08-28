from django.contrib import admin
from .models import Product

class ProductAdimin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)

admin.site.register(Product, ProductAdimin)