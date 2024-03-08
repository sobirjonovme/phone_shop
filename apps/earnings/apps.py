from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EarningsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.earnings'
    verbose_name = _("Daromadlar")
