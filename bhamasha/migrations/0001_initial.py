# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=3)),
                ('aadhar', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('hof_name', models.CharField(max_length=50)),
                ('house_number', models.CharField(max_length=5)),
                ('relations', models.CharField(max_length=20)),
                ('date_of_birth', models.CharField(max_length=20)),
                ('eco_group', models.CharField(max_length=4)),
                ('building_number', models.IntegerField()),
                ('bhamasha_id', models.CharField(max_length=13)),
                ('street_name', models.CharField(max_length=20)),
                ('ifsc_code', models.CharField(max_length=10)),
                ('my_id', models.CharField(max_length=6)),
                ('family_idno', models.CharField(max_length=10)),
                ('pincode', models.IntegerField()),
                ('landline_no', models.IntegerField()),
                ('village_name', models.CharField(max_length=20)),
                ('gp_ward', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('spouse_name', models.CharField(max_length=20)),
                ('is_rural', models.CharField(max_length=4)),
                ('district', models.CharField(max_length=10)),
                ('edu_info', models.CharField(max_length=15)),
                ('account_number', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('income', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=4)),
                ('landmark', models.CharField(max_length=4)),
                ('ration_card_no', models.CharField(max_length=4)),
                ('name_extra', models.CharField(max_length=4)),
                ('mobile_no', models.IntegerField()),
                ('gender', models.CharField(max_length=4)),
                ('father_name', models.CharField(max_length=4)),
                ('fax_no', models.IntegerField()),
                ('block_city', models.CharField(max_length=4)),
                ('created_date', models.DateTimeField(verbose_name='profile creation date')),
            ],
        ),
    ]