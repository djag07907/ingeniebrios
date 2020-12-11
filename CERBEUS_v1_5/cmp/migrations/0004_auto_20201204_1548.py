# Generated by Django 2.2.13 on 2020-12-04 21:48

import cmp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0003_auto_20201129_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasenc',
            name='no_factura',
            field=models.CharField(max_length=100, validators=[cmp.models.validarnumero]),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='contacto',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[cmp.models.validarnombre]),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='descripcion',
            field=models.CharField(max_length=50, unique=True, validators=[cmp.models.validarnombre]),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[cmp.models.validardireccion]),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[cmp.models.validarnumerotelefono]),
        ),
    ]
