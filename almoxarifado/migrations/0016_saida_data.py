# Generated by Django 2.0.5 on 2018-05-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0015_auto_20180510_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='saida',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]