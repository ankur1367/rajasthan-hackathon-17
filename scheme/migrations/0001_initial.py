# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=10)),
                ('scheme_name', models.CharField(max_length=100)),
                ('scheme_desc', models.CharField(max_length=1000)),
                ('sms_body', models.CharField(max_length=160)),
                ('notification_msg_body', models.CharField(max_length=160)),
            ],
        ),
    ]
