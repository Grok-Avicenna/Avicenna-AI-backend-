from django.db import models
from management.models import User
# Create your models here.


class DiseaseCategory(models.Model):

    """Disease category model"""

    title = models.CharField(verbose_name="Disease category title", max_length=255)
    description = models.TextField(verbose_name="Disease category description", blank=True)

    class Meta:
        verbose_name = "Disease category"
        verbose_name_plural = "Disease categories"


class DiseasePost(models.Model):

    """Disease post model """

    sender = models.ForeignKey(
        verbose_name="Disease post sender", to=User,
        on_delete=models.CASCADE, related_name='disease_posts'
    )
    # title = models.CharField(verbose_name="Disease post title", max_length=255)
    title = models.CharField(verbose_name="Title", max_length=150)
    # content = models.TextField("Disease post content")
    # intensity = models.IntegerField("Disease intensity")
    categories = models.ForeignKey(
        verbose_name="Disease category", to=DiseaseCategory,
        on_delete=models.SET_NULL, related_name='disease_posts', null=True
    )
    views = models.ManyToManyField("management.User", related_name='viewed_posts', blank=True)
    created_at = models.DateTimeField(verbose_name="Created date", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated date", auto_now=True)

    class Meta:
        verbose_name = "Disease post"
        verbose_name_plural = "Disease posts"


class DiseasePostAttachments(models.Model):

    """Disease post attachment model """

    disease_post = models.ForeignKey(
        verbose_name="Disease post", to=DiseaseCategory,
        on_delete=models.CASCADE, related_name='attachments'
    )
    # title = models.CharField(verbose_name="Title", max_length=90)
    attachment = models.FileField(verbose_name="Attachment", upload_to='uploads/post_attachments/')

    class Meta:
        verbose_name = "Disease post"
        verbose_name_plural = "Disease posts"


class Answers(models.Model):

    """ Comment Model """

    commentator = models.ForeignKey(to=User, verbose_name="Commentator",
                                    on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(
        verbose_name="Comment post", to=DiseasePost,
        on_delete=models.CASCADE, related_name='comments'
    )
    parent = models.ForeignKey(
        verbose_name="Parent comment", to='self',
        on_delete=models.SET_NULL, related_name='replies', null=True, blank=True
    )

    content = models.TextField(verbose_name="Comment text")
    likes = models.ManyToManyField(verbose_name="Comment likes", to="management.User",
                                   related_name='liked_comments', blank=True)
    dislikes = models.ManyToManyField(verbose_name="Comment dislikes", to="management.User",
                                      related_name='disliked_comments', blank=True)
    # created_at = models.DateTimeField(verbose_name="Create date", auto_now_add=True)
    # updated_at = models.DateTimeField(verbose_name="Update date", auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
