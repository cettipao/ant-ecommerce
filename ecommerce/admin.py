from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'last_price', 'category', 'stock']
    list_display_links = ['title', 'last_price', 'category', 'stock']
    search_fields = ['title',]
    list_filter = ['category',]

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'initial_date', 'final_date', 'total','confirmed',]
    list_display_links = ['user', 'initial_date', 'final_date', 'total', 'confirmed',]
    list_filter = ['user', 'confirmed']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'amount', 'price',]
    list_display_links = ['product', 'cart', 'amount', 'price',]
    list_filter = ['product', 'cart',]

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(StockUp)