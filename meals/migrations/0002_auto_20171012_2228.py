# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='category',
            field=models.IntegerField(choices=[(0, 'First'), (1, 'Second'), (2, 'Third'), (3, 'Forth')], default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='day_linked',
            field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thusday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='source_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='timestamp_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
    ]
