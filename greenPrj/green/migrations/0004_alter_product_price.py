# Generated by Django 4.2.14 on 2024-07-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
