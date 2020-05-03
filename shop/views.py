from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from shop.serializers import ProductSerializer
from shop.serializers import CartSerializer
from shop.serializers import CartProductSerializer
from .models import Product
from .models import Cart


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cart.objects.filter(custID=1)
    serializer_class = CartSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CartProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cart.objects.filter(custID=1)
    serializer_class = CartProductSerializer

# Cart.objects.prefetch_related('productid').get(custID=1)
# Squeryset = queryset.productid.all()

    # queryset = Cart.objects.filter(custID=1).select_related('productid')
    # serializer_class = CartProductSerializer
    # cartitems = CartSerializer(many=True)
    # permission_classes = [permissions.IsAuthenticated]


