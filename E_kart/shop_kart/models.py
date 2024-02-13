from django.db import models
from django.contrib.auth.models import User
import datetime
import os


# Create your models here.

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%d%m%Y%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Catagory(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=1000, null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    quantity=models.IntegerField(blank=False, null=False)
    original_price=models.FloatField(blank=False, null=False)
    selling_price=models.FloatField(blank=False, null=False) 
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=1000, null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Cart(models.Model) :
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)


    
    @property
    def total_cost(self):
        return self.product_qty*self.product.selling_price


class Favourite(models.Model) :
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    name =models.CharField(max_length=200,null=False,blank=False)
    mobile_NO = models.IntegerField(null=False,blank=False)
    pincode = models.IntegerField(null=False,blank=False)
    city = models.CharField(max_length=200,null=False,blank=False)
    address = models.CharField(max_length=1000,null=False,blank=False)
    district =models.CharField(max_length=200,null=False,blank=False)
    state = models.CharField(max_length=200,null=False,blank=False)

    




    



