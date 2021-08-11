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

class CartItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = CartItem
        fields = ['product', 'cart', 'amount', 'price',]

class CartSerializer(serializers.ModelSerializer):
    cartItems = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ecommerce:cartitems-detail'
    )

    class Meta:
        model = Cart
        fields = ['user', 'initial_date', 'final_date', 'confirmed', 'cartItems']

class StockUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockUp
        fields = '__all__'