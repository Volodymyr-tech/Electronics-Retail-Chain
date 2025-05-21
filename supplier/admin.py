from django.contrib import admin

from supplier.models import Node, Product


# Register your models here.
@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "city", "supplier", "debt")
    list_filter = ("city",)
    list_display_links = ("supplier",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date",)