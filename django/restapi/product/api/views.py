from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from product.models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('id','title')