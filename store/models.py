from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price= models.FloatField(null=True)
    digital=models.BooleanField(default=False, null=True , blank=True)
    #image
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=""
        return url



class Order(models.Model):
     customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True, blank=True)
     date_order=models.DateTimeField(auto_now_add=True)
     compleate=models.BooleanField(default=False,null=True, blank=False)
     transaction_id=models.CharField(max_length=200,null=True)

     def __str__(self):
        return str(self.id)
     
     @property  # total amt of order total amt in top of cart page
     def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total


     @property  # total amt of item quantity
     def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product=models.ForeignKey(Product, null=True, blank=True,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order, null=True, blank=True,on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=0,null=True, blank=True)
    date_addedd=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #print("your id value is "+str(type(str(self.id))))
        return str(self.id)
    
    @property  # total amt of order
    def get_total(self):
        total=self.product.price*self.quantity
        return total

class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True, blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True, blank=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_addedd=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    