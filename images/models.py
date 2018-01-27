from django.db import models


class Image(models.Model):

    file = models.FileField()
    location = models.CharField(max_length=80)
    caption = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
