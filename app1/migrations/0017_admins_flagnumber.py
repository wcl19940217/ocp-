# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_remove_admins_flagnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='admins',
            name='flagNumber',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
