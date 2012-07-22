from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField

class Profile(models.Model):

    user = models.ForeignKey(User)
    bio = models.TextField(blank=True, null=True)
    photo = ThumbnailerImageField(upload_to='institution/photo/%Y/%m/%d')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user