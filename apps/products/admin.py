from django.contrib import admin
from unfold import admin as unfold_admin

from .models import Company, Product, ProductType


# Register your models here.
@admin.register(Company)
class CompanyAdmin(unfold_admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")


@admin.register(ProductType)
class ProductTypeAdmin(unfold_admin.ModelAdmin):
    list_display = ("id", "company", "name")
    list_display_links = ("id", "company", "name")
    search_fields = ("id", "company__name", "name")
    list_filter = ("company",)
    autocomplete_fields = ("company",)


@admin.register(Product)
class ProductAdmin(unfold_admin.ModelAdmin):
    list_display = ("id", "company", "product_type", "imei", "is_sold", "purchase_price", "purchased_from", "purchase_date")
    list_display_links = ("id", "company", "product_type", "imei",)
    search_fields = ("id", "company__name", "product_type__name", "imei", "purchased_from",)
    list_filter = ("is_sold", "company", "product_type")
    autocomplete_fields = ("company", "product_type")
