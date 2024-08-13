from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    # thumbnail = models.FileField(upload_to='product_img/',null=True, blank=True)
    
    class Meta:
        ordering = ['id'] 
 
