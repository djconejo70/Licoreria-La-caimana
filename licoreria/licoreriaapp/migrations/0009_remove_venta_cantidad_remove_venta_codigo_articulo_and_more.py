# Generated by Django 4.2.1 on 2023-12-21 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licoreriaapp', '0008_remove_venta_cancelado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='codigo_articulo',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='precio_unidad',
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Total'),
        ),
        migrations.CreateModel(
            name='Venta_detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('precio_unidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Precio/unidad')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='SubTotal')),
                ('codigo_articulo', models.ForeignKey(max_length=6, on_delete=django.db.models.deletion.CASCADE, to='licoreriaapp.articulo')),
                ('codigo_venta', models.ForeignKey(max_length=6, on_delete=django.db.models.deletion.CASCADE, to='licoreriaapp.venta')),
            ],
        ),
    ]