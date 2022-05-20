from django.db import models

class Customers(models.Model):
    name = models.CharField(max_length=100, null=True)
    emil = models.EmailField(max_length=100, null=True)
    mobile = models.BigIntegerField(null=True)
    created_date = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Products(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        ('Anywhere', 'Anywhere')
    )
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    created_date = models.DateField(auto_now_add=True, null=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    category = models.CharField(max_length=100,choices=CATEGORY)

    def __str__(self):
        return self.name


class Orders(models.Model):

    STATUS = (
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
        ('Outfordelivery', 'Outfordelivery')
    )
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE) #check
    product = models.ForeignKey(Products, on_delete=models.CASCADE)   ##check
    created_date = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100,choices=STATUS)

    # def __str__(self):
    #     return self.product

