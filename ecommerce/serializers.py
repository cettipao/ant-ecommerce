from ecommerce.models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'

class StockUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockUp
        fields = '__all__'