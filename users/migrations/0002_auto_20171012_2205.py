# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timestamp_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='user',
            name='timestamp_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
