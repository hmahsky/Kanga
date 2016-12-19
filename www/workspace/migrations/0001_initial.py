# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-16 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboard_name', models.CharField(max_length=40)),
                ('description', models.CharField(default=b'', max_length=80)),
                ('parameters', models.CharField(max_length=1000)),
                ('owner', models.CharField(default=b'', max_length=30)),
            ],
        ),
    ]