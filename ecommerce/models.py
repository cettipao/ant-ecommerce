from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Sum


class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(default="", blank=True)
    image = models.ImageField(null=True, blank=True)

    slug = models.SlugField()

    def __str__(self):
        return self.titulo


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Proveedores"

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    ultimo_precio = models.FloatField()
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    #stock = models.IntegerField()
    descripcion = models.TextField(default="", blank=True)
    image = models.ImageField(null=True, blank=True)

    slug = models.SlugField()

    @property
    def stock(self):
        stockCompra = CompraProducto.objects.filter(producto=self).aggregate(sum=Sum("cantidad")).get("sum")
        stockVenta = ItemCarrito.objects.filter(producto=self, carrito__confirmado=True).aggregate(sum=Sum("cantidad")).get("sum")
        if stockCompra == None:
            stockCompra = 0
        if stockVenta == None:
            stockVenta = 0

        print("{} stockCompra: {}, stockVenta: {}".format(self.titulo, stockCompra, stockVenta))
        return stockCompra - stockVenta

    def __str__(self):
        return self.titulo

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_final = models.DateTimeField(null=True, blank=True)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.usuario.username, self.fecha_inicio)

    @property
    def total(self):
        total = 0
        for itemCarrito in ItemCarrito.objects.filter(carrito=self):
            total += itemCarrito.precio * itemCarrito.cantidad
        return total


class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.SmallIntegerField()
    precio = models.FloatField()

    def __str__(self):
        return "{}: {} ({})".format(self.carrito.usuario.username, self.producto, self.cantidad)

class CompraProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad = models.SmallIntegerField()
    precio = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}: {} ({})".format(self.producto, self.proveedor, self.cantidad)

