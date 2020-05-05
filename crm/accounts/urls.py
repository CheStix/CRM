from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.register_view, name='register_url'),
    path('login/', views.login_view, name='login_url'),
    path('logout/', views.logout_view, name='logout_url'),

    path('', views.home, name='home_url'),
    path('user/', views.user_page, name='user_page_url'),
    path('account/', views.account_settings, name='account_settings_url'),
    path('products/', views.products, name='product_url'),
    path('customer/<int:pk>/', views.customer, name='customer_url'),

    path('create_order/<int:pk>/', views.create_order, name='create_order_url'),
    path('update_order/<int:pk>/', views.update_order, name='update_order_url'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order_url'),

    path('password_reset',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password_reset_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_complete'),

]

#TODO шаблоны для восстановления пароля стилизовать