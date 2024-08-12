from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id', 'name', 'description', 'price', 'quantity')

    # Optional: Add search functionality
    search_fields = ('name', 'description')

    # Optional: Add filters
    list_filter = ('price', 'quantity')

admin.site.register(Product, ProductAdmin)
