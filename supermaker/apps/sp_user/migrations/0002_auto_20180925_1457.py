# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-25 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='手机号码'),
        ),
    ]
