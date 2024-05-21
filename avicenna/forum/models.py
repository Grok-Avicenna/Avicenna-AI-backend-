from django.db import models

# Create your models here.


class DiseaseCategory(models.Model):

    """Disease Category model"""

    title = models.CharField(verbose_name="Title of disease", max_length=255)
    description = models.TextField(verbose_name="Description of disease", blank=True)

    class Meta:
        category = "Disease Category"
        categories = "Disease Categires"


class DiseasePost(models.Model):


    sender = models.ForeignKey(
        verbose_name=_("Disease post sender"), to=User,
        on_delete=models.CASCADE, related_name='disease_posts'
    )