from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Sum


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    image = models.ImageField(null=True, blank=True)

    slug = models.SlugField()

    def __str__(self):
        return self.title


class Supplier(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    last_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True)
    image = models.ImageField(null=True, blank=True)

    slug = models.SlugField()

    @property
    def stock(self):
        boughtStock = StockUp.objects.filter(product=self).aggregate(sum=Sum("amount")).get("sum")
        soldStock = CartItem.objects.filter(product=self, cart__confirmed=True).aggregate(sum=Sum("amount")).get("sum")
        if boughtStock == None:
            boughtStock = 0
        if soldStock == None:
            soldStock = 0

        print("{} stockCompra: {}, stockVenta: {}".format(self.title, boughtStock, soldStock))
        return boughtStock - soldStock

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    initial_date = models.DateTimeField(auto_now_add=True)
    final_date = models.DateTimeField(null=True, blank=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.user.username, self.initial_date)

    @property
    def total(self):
        total = 0
        for itemCart in CartItem.objects.filter(cart=self):
            total += itemCart.price * itemCart.amount
        return total


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.SmallIntegerField()
    price = models.FloatField()

    def __str__(self):
        return "{}: {} ({})".format(self.cart.user.username, self.product, self.amount)

class StockUp(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    amount = models.SmallIntegerField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}: {} ({})".format(self.product, self.supplier, self.amount)

