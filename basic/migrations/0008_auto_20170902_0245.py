# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0007_auto_20170831_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmenthead',
            name='hod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hod', to='basic.User'),
        ),
    ]
