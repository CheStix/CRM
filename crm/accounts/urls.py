from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('products/', views.products, name='product_url'),
    path('customer/<int:pk>/', views.customer, name='customer_url'),
]
