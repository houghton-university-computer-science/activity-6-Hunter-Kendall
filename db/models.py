from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Product(models.Model):
	id = models.BigAutoField(auto_created = True,
                primary_key = True,
                serialize = False, 
                verbose_name ='ID')
	description = models.TextField()
	name = models.CharField(max_length=50)
	price = models.FloatField()
	product_id = models.CharField(max_length=25, unique=True)

class User(AbstractUser):
	def __str__(self):
		return str(self.first_name) + " " + str(self.last_name)

class Customer(models.Model):
	id = models.BigAutoField(auto_created = True,
                primary_key = True,
                serialize = False, 
                verbose_name ='ID')
	user = models.ForeignKey('User', on_delete = models.PROTECT)
	email = models.TextField()
	mailing_address = models.TextField()
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)

class Order(models.Model):
	id = models.BigAutoField(auto_created = True,
                primary_key = True,
                serialize = False, 
                verbose_name ='ID')	
	customer =  models.ForeignKey('Customer', on_delete = models.PROTECT)
	order_date = models.DateField()

class OrderItem(models.Model):
    id = models.BigAutoField(auto_created = True,
            primary_key = True,
            serialize = False, 
            verbose_name ='ID')	
    order = models.ForeignKey('Order', on_delete = models.PROTECT)
    product = models.ForeignKey('Product', on_delete = models.PROTECT)
    quantity = models.IntegerField()
	
	