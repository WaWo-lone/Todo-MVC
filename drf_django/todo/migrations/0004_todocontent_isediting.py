# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-22 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200422_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='todocontent',
            name='isEditing',
            field=models.BooleanField(default=False, verbose_name='编辑状态'),
        ),
    ]
