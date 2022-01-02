from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product, Seller, Category

# Create your views here.

class ProductList(APIView):
    """
    List all products or create new one
    """
    def get(self, request):
        products = Product.objects.all()
        # serializer!!!