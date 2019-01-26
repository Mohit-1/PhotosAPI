from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    pid = models.IntegerField(primary_key=True)
    owner = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True)
    photo_url = models.CharField(max_length=300) # Inspect URLField's use

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return self.title + " " + self.owner


class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)
    no_of_photos = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.name
