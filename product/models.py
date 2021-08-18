from django.db import models
from django.utils import timezone


# Create your models here.

# Product model for porducts
class Product(models.Model):
    product_id= models.AutoField
    product_name = models.CharField(max_length=200)
    product_pice = models.DecimalField(max_digits=10, decimal_places=2)
    product_weight = models.IntegerField()
    category = models.CharField(max_length=60,default="")
    date_time = models.DateField(default = timezone.now)
    image=models.ImageField(upload_to='product/images',default="")


    def __str__(self):
        return str(self.product_name) + ": Rs" + str(self.product_pice)


# orderupdte of single porduct
class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
