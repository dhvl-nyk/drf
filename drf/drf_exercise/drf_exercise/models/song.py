from django.db import models
from django import forms
# from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import HStoreField,ArrayField
from jsonfield import JSONField

class Song(models.Model):
    artist_name = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    similars = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    track_id = models.TextField()
    title = models.TextField()

    def __str__(self):
      return self.track_id

class Tag(models.Model):
    tag_name = models.TextField()
    score = models.IntegerField()
    songs = models.ManyToManyField(Song, related_name='tags')

    def __str__(self):
        return self.tag_name
