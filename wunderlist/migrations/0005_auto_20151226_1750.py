# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wunderlist', '0004_auto_20151226_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connection',
            name='todo_list',
        ),
        migrations.AddField(
            model_name='connection',
            name='list_id',
            field=models.IntegerField(default=0, verbose_name='List ID'),
            preserve_default=False,
        ),
    ]
