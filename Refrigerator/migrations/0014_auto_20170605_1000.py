# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Refrigerator', '0013_auto_20170603_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_image',
            field=models.FileField(blank=True, default=b'', upload_to=b''),
        ),
    ]