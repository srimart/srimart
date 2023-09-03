from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import *

urlpatterns=[
    path('',views.home,name='home'),
    path('profile/',views.create_customer,name='create_customer'),
    path('productdetails/<int:pk>',views.productdetails,name='productdetails'),
    path('addtocart/<int:pk>',views.addtocart,name='addtocart'),
    path('cart',views.cart,name='cart'),
    path('createcustomer/', views.create_customer, name='create-customer'),
    path('userdetailsdelete/<int:pk>', views.deletecustomer, name='deletecustomer'),
    path('placeorder/', views.placedorder, name='placedorder'),
    path('orders/', views.orderplaced, name='orderplaced'),
    path('deletecartproduct/<int:product_id>',views.delete_cart_product,name='delete_cart_product'),
    path('contact/', views.contact, name='contact'),
    path('cancelorder/<int:pk>',views.cancelOrder,name='cancelorder'),




 

    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
]