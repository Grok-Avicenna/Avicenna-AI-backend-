from django.db import models
from django.conf import settings
from datetime import date
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone

# Create your models here.


class User(AbstractUser, PermissionsMixin):

    """ User model """

    avatar = models.ImageField(verbose_name="Image", upload_to="avatars/", default=settings.NO_AVATAR)
    phone = models.CharField(verbose_name="phone number", max_length=15, unique=True)

    middle_name = models.CharField(verbose_name="Middle name", max_length=50)
    birth_date = models.DateField(verbose_name=_("Birth date"), default=date(2000, 1, 1), blank=True)

    verify_code = models.PositiveSmallIntegerField(verbose_name="Verify code", default=0)
    verify_time = models.DateField(verbose_name="Verify time", default=timezone.now)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    user_type = models.CharField(verbose_name="User's type", max_length=10, )





