
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter() 
router.register('', views.ProductViewset , basename='products') 

urlpatterns = [
    path('', include(router.urls)),
]