from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

# Create your models here.


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(verbose_name=_(
        "Date of birth"), blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    address1 = models.CharField(verbose_name=_(
        "Address line 1"), max_length=1024, blank=True, null=True)
    zip_code = models.CharField(verbose_name=_(
        "Postal Code"), max_length=12, blank=True, null=True)
    city = models.CharField(verbose_name=_(
        "City"), max_length=1024, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=_(
        "Enter a valid international mobile phone number starting with +(country code)"))
    mobile_phone = models.CharField(validators=[phone_regex], verbose_name=_(
        "Mobile phone"), max_length=17, blank=True, null=True)
    photo = models.ImageField(verbose_name=_(
        "Photo"), upload_to='photos/', default='photos/default-user-avatar.png')

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
