# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-09 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]