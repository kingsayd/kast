from django.contrib import admin
from .models import product
# Register your models here.

class productAdmin(admin.ModelAdmin):

    list_display = ('product_name','price','stock','category','created_date','modified_date')
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(product, productAdmin)
