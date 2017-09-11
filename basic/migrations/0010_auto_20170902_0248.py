# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0009_auto_20170902_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmenthead',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='departmenthead',
            name='temp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temp', to='basic.User'),
        ),
    ]
