from django.shortcuts import render
from rest_framework import viewsets, filters
from product.models import Product
from .serializer import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ProductView(viewsets.ModelViewSet):
     queryset=Product.objects.all()
     serializer_class = ProductSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['category', 'country']  # Add filters for category and country
     search_fields = ['name', 'description']  # Add search functionality for name and description

# def test(request):
#     return HttpResponse('hello')