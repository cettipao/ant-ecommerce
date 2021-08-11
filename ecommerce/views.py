from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .models import *
from .serializers import *
from rest_framework import viewsets


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = []

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Cart.objects.all()
        return Cart.objects.filter(user=user)



class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        cart = self.request.query_params.get('cart')
        if user.is_superuser:
            return CartItem.objects.all()
        else:
            if cart:
                if Cart.objects.get(id=cart).user == user:
                    return CartItem.objects.filter(cart__user=user)
                else:
                    raise PermissionDenied({"message": "You don't have permission to access"})
            else:
                raise PermissionDenied({"message": "please select a cart"})

class StockUpViewSet(viewsets.ModelViewSet):
    queryset = StockUp.objects.all()
    serializer_class = StockUpSerializer
    permission_classes = []
