# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 13:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0002_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='classe_tipo_produto',
            new_name='classe_produto',
        ),
    ]
