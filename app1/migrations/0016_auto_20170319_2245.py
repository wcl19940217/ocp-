# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_tag_isdelete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admins',
            name='flagNumber',
        ),
        migrations.AddField(
            model_name='admins',
            name='group_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='admins',
            name='parentId',
            field=models.CharField(default='', max_length=30),
        ),
    ]
