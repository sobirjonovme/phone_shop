from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


# Create your models here.
class SoldProduct(BaseModel):
    product = models.ForeignKey(
        verbose_name=_("Mahsulot"),
        to="products.Product",
        on_delete=models.CASCADE,
        related_name="sold_products"
    )
    sold_price = models.DecimalField(
        verbose_name=_("Sotilgan narx"), max_digits=13, decimal_places=2
    )
    client = models.CharField(
        verbose_name=_("Mijoz"), max_length=255, null=True, blank=True
    )
    sold_date = models.DateField(
        verbose_name=_("Sotilgan sana"), null=True, blank=True
    )
    comment = models.TextField(
        verbose_name=_("Izoh"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Sotilgan mahsulot")
        verbose_name_plural = _("Sotilgan mahsulotlar")

    def __str__(self):
        return str(self.product)


class OtherIncome(BaseModel):
    amount = models.DecimalField(
        verbose_name=_("Summa"), max_digits=13, decimal_places=2
    )
    comment = models.TextField(
        verbose_name=_("Izoh"), null=True, blank=True
    )
    date = models.DateField(
        verbose_name=_("Sana"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Boshqa daromad")
        verbose_name_plural = _("Boshqa daromadlar")

    def __str__(self):
        return str(self.amount)
