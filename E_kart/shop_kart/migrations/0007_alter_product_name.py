# Generated by Django 5.0 on 2024-02-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_kart', '0006_remove_favourite_product_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
