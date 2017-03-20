# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bhamasha', '0002_auto_20170320_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyinfo',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familyinfo', to='bhamasha.Info'),
        ),
        migrations.AlterField(
            model_name='info',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]