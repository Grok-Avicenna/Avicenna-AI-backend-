from django.db import models
from django.utils.translation import gettext_lazy as _


class UserTypeChoices(models.TextChoices):

    DOCTOR = 'doctor', _('Doctor')

    PATIENT = 'patient', _('Patient')


class GenderChoices(models.TextChoices):

    MALE = 'male', _('Male')

    FEMALE = 'female', _('Female')


class SocialGroupChoices(models.TextChoices):

    CHILD = 'child', _('Child')

    ADULTS = 'adult', _('Adult')

    PENSIONERS = 'pensioner', _('Pensioner')

    DISABLED = 'disabled', _('Disabled')


class ProfessionChoices(models.TextChoices):

    FARMER = 'farmer', _('Farmer')

    WORKER = 'worker', _('Worker')

    EMPLOYEE = 'employee', _('Employee')

    FREELANCER = 'freelancer', _('Freelancer')

    PRIEST = 'priest', _('Priest')

    OTHER = 'other', _('Other')
