# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ver', '0002_auto_20170727_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='phone',
            field=models.ForeignKey(db_column='UserData.id', on_delete=django.db.models.deletion.CASCADE, to='Reg.UserData'),
        ),
    ]