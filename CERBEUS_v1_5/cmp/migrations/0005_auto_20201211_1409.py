# Generated by Django 2.2.13 on 2020-12-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0004_auto_20201204_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
