# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-10 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180409_1922'),
        ('travel', '0002_auto_20180409_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='favorites',
        ),
        migrations.AddField(
            model_name='trip',
            name='allusers',
            field=models.ManyToManyField(related_name='allTrips', to='login.User'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addedTrips', to='login.User'),
        ),
    ]