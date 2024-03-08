from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


# Create your models here.
class Company(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Ishlab chiqaruvchi")
        verbose_name_plural = _("Ishlab chiqaruvchilar")

    def __str__(self):
        return self.name


class ProductType(BaseModel):
    company = models.ForeignKey(
        verbose_name=_("Ishlab chiqaruvchi"),
        to=Company,
        on_delete=models.CASCADE,
        related_name="product_types"
    )
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Mahsulot turi")
        verbose_name_plural = _("Mahsulot turlari")

    def __str__(self):
        return self.name


class Product(BaseModel):
    company = models.ForeignKey(
        verbose_name=_("Ishlab chiqaruvchi"),
        to=Company,
        on_delete=models.CASCADE,
        related_name="products"
    )
    product_type = models.ForeignKey(
        verbose_name=_("Mahsulot turi"),
        to=ProductType,
        on_delete=models.CASCADE,
        related_name="products"
    )
    imei = models.CharField(
        verbose_name=_("IMEI"), max_length=255, unique=True
    )
    purchase_price = models.DecimalField(
        verbose_name=_("Xarid qilingan narx"), max_digits=13, decimal_places=2
    )
    status = models.CharField(
        verbose_name=_("Holati"), max_length=255, null=True, blank=True
    )
    purchased_from = models.CharField(
        verbose_name=_("Xarid qilingan joy/odam"), max_length=255, null=True, blank=True
    )
    purchase_date = models.DateField(
        verbose_name=_("Xarid qilingan sana"), null=True, blank=True
    )
    is_sold = models.BooleanField(
        verbose_name=_("Sotilganmi?"), default=False
    )

    class Meta:
        verbose_name = _("Mahsulot")
        verbose_name_plural = _("Mahsulotlar")

    def __str__(self):
        return f"#{self.id} - {self.imei} - {self.product_type.name}"
