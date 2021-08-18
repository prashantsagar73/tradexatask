from django.contrib import admin
from .models import Product, OrderUpdate

# Register your models here.
admin.site.register((Product,OrderUpdate))