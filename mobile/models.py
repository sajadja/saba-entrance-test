from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.common_models import BaseModel
from django_countries.fields import CountryField


class Mobile(BaseModel):
    brand_name = models.CharField(_('نام برند'), max_length=150)
    brand_nationality = CountryField(_('ملیت برند'))
    model = models.CharField(_('مدل'), max_length=150, unique=True)
    price = models.PositiveBigIntegerField(_('قیمت'))
    color = models.CharField(_('رنگ'), max_length=150)
    screen_size = models.FloatField(_('سایز صفحه نمایش'))
    is_availble = models.BooleanField(_('وضعیت'))
    made_in = CountryField(_('کشور سازنده'))

    def __str__(self):
        return self.model
