# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20170219_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actregistration',
            name='isInner',
            field=models.BooleanField(default=True),
        ),
    ]
