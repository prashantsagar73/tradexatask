from django.contrib import admin
from .models import Product, OrdersCreate,OrderUpdate

# Register your models here.
admin.site.register((Product,OrdersCreate,OrderUpdate))