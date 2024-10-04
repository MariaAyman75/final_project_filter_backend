from django.db import models


# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Dessert', 'Dessert'),
    ]   
    COUNTRY_CHOICES = [
        ('Fayoum','Fayoum'),
        ('Cairo','Cairo'),
        ('Alexandria','Alexandria')
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)

    def __str__(self):
        return self.name
