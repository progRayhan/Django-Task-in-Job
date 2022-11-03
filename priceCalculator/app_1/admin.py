from django.contrib import admin
from app_1.models import Product, Category 

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'price', 'amount', 'total_price', 'category','discount_price', 'save_price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)