# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-06 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20170706_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='first_step',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='checklistname', to='backend.CheckListStep'),
        ),
        migrations.AlterField(
            model_name='checkliststep',
            name='first_children',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='checkliststepparent', to='backend.CheckListStep'),
        ),
        migrations.AlterField(
            model_name='checkliststep',
            name='next_step',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='last_step', to='backend.CheckListStep'),
        ),
    ]