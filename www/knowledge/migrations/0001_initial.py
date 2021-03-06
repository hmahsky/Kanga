# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-16 08:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=100)),
                ('query', models.TextField(default=b'')),
                ('description', models.TextField(default=b'')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
                ('scheduled_time', models.CharField(default=b'', max_length=50)),
                ('scheduled', models.BooleanField(default=False)),
                ('cron_schedule', models.CharField(default=b'', max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BatchQueryPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readable', models.BooleanField(default=False)),
                ('writable', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledge.BatchQuery')),
            ],
        ),
        migrations.CreateModel(
            name='QueryLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField(default=b'')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledge.BatchQuery')),
            ],
        ),
        migrations.CreateModel(
            name='RealtimeQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=100)),
                ('query', models.TextField(default=b'')),
                ('description', models.TextField(default=b'')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('running', models.BooleanField(default=False)),
                ('local_mode', models.BooleanField(default=False)),
                ('query_option', models.TextField(default=b'')),
                ('last_running', models.CharField(default=b'', max_length=50)),
                ('jar_path', models.CharField(default=b'', max_length=250)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RealtimeQueryPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readable', models.BooleanField(default=False)),
                ('writable', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledge.RealtimeQuery')),
            ],
        ),
    ]
