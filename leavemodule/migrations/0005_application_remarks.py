# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leavemodule', '0004_auto_20170827_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='remarks',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
