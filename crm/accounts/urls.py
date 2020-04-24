from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_view, name='register_url'),
    path('login/', views.login_view, name='login_url'),
    path('logout/', views.logout_view, name='logout_url'),

    path('', views.home, name='home_url'),
    path('products/', views.products, name='product_url'),
    path('customer/<int:pk>/', views.customer, name='customer_url'),

    path('create_order/<int:pk>/', views.create_order, name='create_order_url'),
    path('update_order/<int:pk>/', views.update_order, name='update_order_url'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order_url'),
]
