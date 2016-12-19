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
            name='JobTitle',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restrict_search_terms', models.CharField(default=100, max_length=50)),
                ('restrict_search_timerange', models.IntegerField(default=-1)),
                ('userlevel_concurrent_searchjobs_limit', models.IntegerField(default=3)),
                ('Userlevel_concurrent_realtime_searchjobs_limit', models.IntegerField(default=6)),
                ('rolelevel_concurrent_searchjobs_limit', models.IntegerField(default=50)),
                ('rolelevel_concurrent_realtime_searchjobs_limit', models.IntegerField(default=100)),
                ('limit_total_jobs_disk_quota', models.IntegerField(default=100)),
                ('selected_indexes', models.CharField(max_length=50)),
                ('selected_search_indexes', models.CharField(max_length=50)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('selected_roles', models.ManyToManyField(related_name='_role_selected_roles_+', to='account.Role')),
            ],
        ),
        migrations.CreateModel(
            name='UserActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('activation_hashcode', models.CharField(max_length=50)),
                ('passwordchange_hashcode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_hashcode', models.CharField(blank=True, default=b'', max_length=50)),
                ('password_change_hashcode', models.CharField(blank=True, default=b'', max_length=50)),
                ('job_title', models.ForeignKey(default=b'Kanga Administrator', on_delete=django.db.models.deletion.CASCADE, to='account.JobTitle')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]