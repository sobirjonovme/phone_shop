# Generated by Django 4.2.10 on 2024-03-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_producttype_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sold',
            field=models.BooleanField(default=False, verbose_name='Sotilganmi?'),
        ),
    ]