# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0010_merge_20180330_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='data',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='fornecedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='almoxarifado.Fornecedor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entrada',
            name='itens',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='almoxarifado.ItemEntrada'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entrada',
            name='nota_Fiscal',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itementrada',
            name='material',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='almoxarifado.Material'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itementrada',
            name='quantidade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itementrada',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='material',
            name='categoria',
            field=models.CharField(choices=[('estocavel', 'Estoc\xe1vel'), ('n_estocavel', 'N\xe3o estoc\xe1vel'), ('cons_geral', 'Consumo geral'), ('manutencao', 'Manuten\xe7\xe3o')], max_length=255),
        ),
    ]
