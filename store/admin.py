from django.contrib import admin
from django.forms import ModelForm
from .models import Product


# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    # form = ProductForm
    prepopulated_fields = {
        'slug': ('product_name', )
    }
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')


admin.site.register(Product, ProductAdmin)

