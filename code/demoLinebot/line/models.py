# Create your models here.
from django.db import models


class Sticker(models.Model):
    packageId = models.PositiveIntegerField()  
    stickerId = models.PositiveIntegerField()  
    keywords = models.CharField(max_length = 500,null = True,default = "", blank=True)  
    url = models.CharField(max_length =200)
    
class Restaurant(models.Model):
    name = models.CharField(max_length = 500,null = False,blank = False)  
    address = models.CharField(max_length = 500,null = False,blank = False) 
    image_url = models.CharField(max_length = 500,null = False,blank = False) 
    telephone = models.CharField(max_length = 500,null = False,blank = False)  
    business_hours  = models.TextField(max_length = 500,null = False,blank = False)  
    show_name = models.CharField(max_length = 500,null = False,blank = False)  
    date = models.DateField(auto_now=False, auto_now_add=False)
    points = models.PositiveIntegerField()  
