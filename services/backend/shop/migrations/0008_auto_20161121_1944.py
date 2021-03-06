# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 19:44
from __future__ import unicode_literals

from django.db import migrations, models

import shop.utils


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_category_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=shop.utils.UploadHashedTo('items')),
        ),
    ]
