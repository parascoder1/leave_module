# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0017_auto_20170902_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmenthead',
            name='till',
            field=models.DateField(),
        ),
    ]
