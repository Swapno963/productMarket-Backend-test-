from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters

# Create your views here.
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 100
    
class ProductViewset(viewsets.ModelViewSet):
    pagination_class = CustomPagination
    queryset = models.Product.objects.all().order_by('id')
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter]
    # search_fields = ['name']
