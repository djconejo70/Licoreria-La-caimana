# Generated by Django 4.2.1 on 2023-11-01 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licoreriaapp', '0007_rename_articulo_venta_codigo_articulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cancelado',
        ),
    ]