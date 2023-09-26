from django.db import models
from django.urls import reverse


class category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    discription = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photo/categories', blank=True)


class meta:
    verbose_name='category'
    verbose_name_plural='categories'

def get_url(self):
    return reverse('product_by_category', args=[self.slug])

def __str__(self):
    return self.category_name
