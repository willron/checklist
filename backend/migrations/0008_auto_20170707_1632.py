# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-07 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20170706_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkliststep',
            name='checklist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='step_list', to='backend.CheckList'),
        ),
    ]
