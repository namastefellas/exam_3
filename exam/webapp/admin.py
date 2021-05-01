from django.contrib import admin
from webapp.models import Product, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'pic']
    fields = ['name', 'description', 'category', 'pic']
    readonly_fields = ['id']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'author', 'description', 'score', 'created_at', 'updated_at']
    fields = ['author', 'product', 'description', 'score', 'moderated']

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)