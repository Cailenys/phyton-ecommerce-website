from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug= models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    def _str_(self): 
      return self.name

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug= models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)