# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-06-05 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bunk', '0002_auto_20190605_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='time_bunked_on',
            new_name='times_bunked_on',
        ),
    ]
