# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Refrigerator', '0015_auto_20170618_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_image',
            field=models.IntegerField(max_length=50),
        ),
    ]
