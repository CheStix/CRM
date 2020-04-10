from django.contrib import admin

from .models import Customer, Product, Order, Tag


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date_created']


@admin.register(Tag)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name']
