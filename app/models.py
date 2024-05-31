from django.db import models
class Product(models.Model):

    product_name=models.CharField(null=True,max_length=100)
    product_code=models.CharField(max_length=100,null=True)
    product_price = models.IntegerField(null=True)
    product_GST=models.FloatField(null=True)
    food_product=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    def __str__(self):
        return self.title
    
class Product(models.Model):
    
    product_name=models.CharField(null=True,max_length=100)
    product_code=models.CharField(max_length=100,null=True)
    product_price = models.IntegerField(null=True)
    product_GST=models.FloatField(null=True)
    food_product=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    def __str__(self):
        return self.title



# Create your models here.
