# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0003_auto_20180322_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='observacao',
            field=models.TextField(default='Digite aqui', max_length=400),
        ),
        migrations.AlterField(
            model_name='produto',
            name='classe_produto',
            field=models.CharField(choices=[('estocavel', 'Estoc\xe1vel'), ('n_estocavel', 'N\xe3o estoc\xe1vel'), ('cons_geral', 'Consumo geral'), ('manutencao', 'Manuten\xe7\xe3o')], max_length=255),
        ),
    ]
