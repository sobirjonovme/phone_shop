from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from unfold import admin as unfold_admin

from .models import SoldProduct, OtherIncome


# Register your models here.
@admin.register(SoldProduct)
class SoldProductAdmin(unfold_admin.ModelAdmin):
    list_display = ("id", "product_type", "imei", "status", "purchase_price", "sold_price", "sold_date")
    list_display_links = ("id", "product_type", "imei")
    search_fields = ("id", "product__product_type__name", "imei",)
    list_filter = ("product__product_type", "product__company",)
    autocomplete_fields = ("product",)
    readonly_fields = ("product_type", "imei", "status", "purchase_price")

    def product_type(self, obj):
        return obj.product.product_type.name or "-"

    def imei(self, obj):
        return obj.product.imei or "-"

    def status(self, obj):
        return obj.product.status or "-"

    def purchase_price(self, obj):
        return obj.product.purchase_price or "-"

    product_type.short_description = _("Mahsulot turi")
    imei.short_description = _("IMEI")
    status.short_description = _("Holati")
    purchase_price.short_description = _("Xarid qilingan narx")


@admin.register(OtherIncome)
class OtherIncomeAdmin(unfold_admin.ModelAdmin):
    list_display = ("id", "amount", "date", "comment",)
    list_display_links = ("id", "amount", "date")
    search_fields = ("id", "comment",)
