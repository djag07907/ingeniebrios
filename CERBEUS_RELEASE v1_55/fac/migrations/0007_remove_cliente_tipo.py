# Generated by Django 2.2.13 on 2020-12-18 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0006_auto_20201218_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='tipo',
        ),
    ]
