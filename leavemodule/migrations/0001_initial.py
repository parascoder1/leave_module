# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basic', '0002_auto_20170826_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('type_of_leave', models.CharField(max_length=100)),
                ('from_date', models.DateField()),
                ('till_date', models.DateField()),
                ('acad_pf', models.IntegerField()),
                ('admin_pf', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('purpose', models.CharField(max_length=500)),
                ('date_of_app', models.DateField()),
                ('is_station', models.BooleanField(default='false')),
                ('pf', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Leave_credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casual', models.IntegerField()),
                ('restricted', models.IntegerField()),
                ('sp_casual', models.IntegerField()),
                ('earned', models.IntegerField()),
                ('commuted', models.IntegerField()),
                ('vacation', models.IntegerField()),
                ('pf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.User')),
            ],
        ),
    ]
