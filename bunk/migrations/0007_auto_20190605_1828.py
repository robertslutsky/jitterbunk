# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-06-05 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bunk', '0006_auto_20190605_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk',
            name='bunkee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bunks_in', to='bunk.Person'),
        ),
        migrations.AlterField(
            model_name='bunk',
            name='bunker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bunks_out', to='bunk.Person'),
        ),
    ]
