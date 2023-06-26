from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=150,blank=False,null=False,unique=True)
    description=models.TextField(null=False)
    cat_image=models.ImageField(upload_to='images/category')

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True,blank=True)
    prod_image=models.ImageField(upload_to='images/products')
    prod_description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name



