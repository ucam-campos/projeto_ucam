# Generated by Django 2.0.3 on 2018-03-27 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0006_auto_20180327_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('abreviacao', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='produto',
            name='unidade_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='almoxarifado.UnidadeMedida'),
        ),
    ]