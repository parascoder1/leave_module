# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leavemodule', '0030_auto_20170902_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='ap_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leavemodule.Application'),
        ),
    ]
