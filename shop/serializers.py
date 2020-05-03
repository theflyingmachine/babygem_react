from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product
from .models import Cart


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'imgurl', 'description']


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['productid', 'custID', 'quantity']


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'quantity', 'name']
        # fields = ['id', 'custID', 'quantity']
