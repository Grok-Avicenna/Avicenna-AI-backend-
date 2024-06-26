# Generated by Django 5.0.6 on 2024-05-22 05:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forum', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='commentator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Commentator'),
        ),
        migrations.AddField(
            model_name='answers',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='disliked_comments', to=settings.AUTH_USER_MODEL, verbose_name='Comment dislikes'),
        ),
        migrations.AddField(
            model_name='answers',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to=settings.AUTH_USER_MODEL, verbose_name='Comment likes'),
        ),
        migrations.AddField(
            model_name='answers',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='forum.answers', verbose_name='Parent comment'),
        ),
        migrations.AddField(
            model_name='diseasepost',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disease_posts', to='forum.diseasecategory', verbose_name='Disease category'),
        ),
        migrations.AddField(
            model_name='diseasepost',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disease_posts', to=settings.AUTH_USER_MODEL, verbose_name='Disease post sender'),
        ),
        migrations.AddField(
            model_name='diseasepost',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='viewed_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answers',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.diseasepost', verbose_name='Comment post'),
        ),
        migrations.AddField(
            model_name='diseasepostattachments',
            name='disease_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='forum.diseasecategory', verbose_name='Disease post'),
        ),
    ]
