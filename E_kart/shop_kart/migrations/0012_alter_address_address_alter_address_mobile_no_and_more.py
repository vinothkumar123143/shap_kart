# Generated by Django 5.0 on 2024-02-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_kart', '0011_alter_address_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='address',
            name='mobile_NO',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
