from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class article(models.Model):
    """ This model stores the article data and information"""
    article_heading = models.TextField()
    article_head_lc_lang = models.TextField()
    article = models.TextField()
    group = models.CharField(max_length=255)
    sub_grp = models.CharField(max_length=255)
    publish_status = models.CharField(max_length=5)
    proof_read_by = models.CharField(max_length=255)
    content_dtp_person = models.CharField(max_length=255)
    content_created_by = models.CharField(max_length=255)
    image_name = models.CharField(max_length=255)
    create_datetime = models.DateTimeField(default=datetime.now())
    publish_datetime = models.DateTimeField(default=datetime.now())
    will_expire = models.BooleanField(default=False)
    expire_date = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.article_heading