from django.db import models
from django.contrib.auth.models import User


class Address_Details(models.Model):
    house_number = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    subdivision = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.IntegerField(default=0)
    country = models.CharField(max_length=200)
    
    #(House #, Street, Subdivision, City, Postal Code, Country)
    def __str__(self):
        return '('+ self.house_number +', '+ self.street +', '+ self.subdivision +', '+ self.city +', '+ str(self.postal_code) +', '+ self.country +')'
    
    class Meta:
        verbose_name_plural = "Address_Details"

class User_Details(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    billing_address = models.ForeignKey(Address_Details, on_delete=models.CASCADE, related_name ="billing_address")
    shipping_address = models.ForeignKey(Address_Details, on_delete=models.CASCADE,related_name ="shipping_address")
    
    def __str__(self):
        return str(self.user_id) +', '+ self.first_name +' '+ self.last_name
    
    class Meta:
        verbose_name_plural = "User_Details"
    

class Product(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    item_photo = models.FileField(blank=True,null=True)
    item_name = models.CharField(max_length=200)
    item_quantity = models.IntegerField(default=0)
    item_price = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    isPurchased = models.BooleanField(default=False)
    
    type_choice = (
        ('Analog', 'Analog watch'),
        ('Digital', 'Digital watch'),
        ('Smart', 'Smart watch'),
    )
    
    item_type = models.CharField(max_length=50, choices=type_choice, default=type_choice[0][0])
    
    def __str__(self):
        return self.item_name +' ('+str(self.id)+') '
