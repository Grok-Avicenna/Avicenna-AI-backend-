from django.db import models
from django.conf import settings
from datetime import date
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
from .choices import UserTypeChoices, SocialGroupChoices



# Create your models here.


class User(AbstractUser, PermissionsMixin):

    """ User model """

    avatar = models.ImageField(verbose_name="Avatar", upload_to="avatars/", default=settings.NO_AVATAR)
    phone = models.CharField(verbose_name="phone number", max_length=15, unique=True)
    id_card_photo = models.ImageField(verbose_name="Passport's photo", upload_to="Passports/")

    full_name = models.CharField(verbose_name="Full name", max_length=50)
    birth_date = models.DateField(verbose_name="Birth date", default=date(2000, 1, 1), blank=True)

    verify_code = models.PositiveSmallIntegerField(verbose_name="Verify code", default=0)
    verify_time = models.DateField(verbose_name="Verify time", default=timezone.now)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    user_type = models.CharField(verbose_name="User's type", max_length=10, choices=UserTypeChoices.choices)


class Doctor(models.Model):

    """ Doctor model """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor")
    experience = models.CharField(verbose_name="Experience", null=True, max_length=5)

    work_time_start = models.TimeField("Start of working")
    end_time_start = models.TimeField("End of working")

    schedule = models.CharField(verbose_name="Schedule", max_length=255)
    educations = models.FileField(verbose_name="Files of cerificates", upload_to="diplomas/")

    is_verified = models.BooleanField(verbose_name="Is doctor verified?")

    class Meta:
        db_table = "doctor"
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"


class Patient(models.Model):

    """ Patient User Model """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient")
    age = models.CharField(verbose_name="Age of patient", max_length=10, choices=SocialGroupChoices.choices)

    class Meta:
        db_table = "patient"
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
