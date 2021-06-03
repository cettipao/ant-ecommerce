from django.contrib import admin
from .models import *

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ultimo_precio', 'category', 'stock']
    list_display_links = ['titulo', 'ultimo_precio', 'category', 'stock']
    search_fields = ['titlo',]
    list_filter = ['category',]

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha_inicio', 'fecha_final', 'total','confirmado',]
    list_display_links = ['usuario', 'fecha_inicio', 'fecha_final', 'total', 'confirmado',]
    list_filter = ['usuario', 'confirmado']

class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'carrito', 'cantidad', 'precio',]
    list_display_links = ['producto', 'carrito', 'cantidad', 'precio',]
    list_filter = ['producto', 'carrito',]

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ItemCarrito, ItemCarritoAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(CompraProducto)