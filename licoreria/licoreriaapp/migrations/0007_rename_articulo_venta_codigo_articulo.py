# Generated by Django 4.2.1 on 2023-07-13 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licoreriaapp', '0006_alter_venta_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='articulo',
            new_name='codigo_articulo',
        ),
    ]
