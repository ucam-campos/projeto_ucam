# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 13:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0006_report'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Report',
        ),
    ]