from rest_framework import serializers
from app_1.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['name', 'price', 'amount', 'category', 'total_price']
        fields = ['name', 'price', 'amount', 'total_price', 'category','discount_price', 'save_price']