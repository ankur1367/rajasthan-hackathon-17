from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Scheme(models.Model):
    department = models.CharField(max_length=100)
    scheme_name = models.CharField(max_length=100)
    scheme_desc = models.CharField(max_length=1000)
    sms_body = models.CharField(max_length=160)
    notification_msg_body = models.CharField(max_length=160)
    created_date = models.DateTimeField()

    def __unicode__(self):
        return '%s' % ( self.scheme_name)
