# Generated by Django 5.0 on 2024-02-09 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_kart', '0010_alter_address_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=500),
        ),
    ]