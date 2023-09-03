from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Customer, Cart, OrderdItems, Contact
from django.contrib.auth.models import User

# Customizing admin header and title
admin.site.site_header = "Sree mart"
admin.site.site_title = "Admin Panel"

# ModelAdmin classes
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'prize')
    list_filter = ('prize',)
    search_fields = ('name', 'description')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')
    list_filter = ('state',)
    search_fields = ('name', 'city')

class OrderdItemsAdmin(admin.ModelAdmin):
    list_display = ('user', 'products', 'customer', 'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'products__name')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

# Registering models with custom ModelAdmin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart)
admin.site.register(OrderdItems, OrderdItemsAdmin)
admin.site.register(Contact, ContactAdmin)

# Unregistering the Group model
admin.site.unregister(Group)
