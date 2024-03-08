from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here
class User(AbstractUser):
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        name = f"{self.first_name} {self.last_name}" if self.first_name else self.username
        return name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
