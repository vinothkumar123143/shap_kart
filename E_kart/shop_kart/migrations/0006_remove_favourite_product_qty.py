# Generated by Django 5.0 on 2024-02-04 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_kart', '0005_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='product_qty',
        ),
    ]
