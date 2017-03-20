# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bhamasha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyInfo',
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
                ('bank_name', models.CharField(max_length=40)),
                ('landmark', models.CharField(max_length=40)),
                ('ration_card_no', models.CharField(max_length=15)),
                ('name_extra', models.CharField(max_length=24)),
                ('mobile_no', models.IntegerField()),
                ('gender', models.CharField(max_length=8)),
                ('father_name', models.CharField(max_length=50)),
                ('fax_no', models.IntegerField()),
                ('block_city', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(verbose_name='profile creation date')),
            ],
        ),
        migrations.AlterField(
            model_name='info',
            name='bank_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='block_city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='info',
            name='father_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='info',
            name='gender',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='info',
            name='landmark',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='name_extra',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='info',
            name='ration_card_no',
            field=models.CharField(max_length=15),
        ),
        migrations.AddField(
            model_name='familyinfo',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bhamasha.Info'),
        ),
    ]