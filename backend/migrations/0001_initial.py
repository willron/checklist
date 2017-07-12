# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-06 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CheckListStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.CheckList')),
                ('next_step', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.CheckListStep')),
                ('parent_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children_step', to='backend.CheckListStep')),
            ],
        ),
    ]