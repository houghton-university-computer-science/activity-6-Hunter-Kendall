from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from db.models import User, Product, Order, OrderItem, Customer

admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderItem)
# Register your models here.
