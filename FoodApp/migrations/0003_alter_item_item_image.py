# Generated by Django 5.0.4 on 2024-04-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://t3.ftcdn.net/jpg/04/17/41/92/360_F_417419275_y8vQY8TXGRpQGpsgkkqihUaWpmtukRhY.jpg', max_length=5000),
        ),
    ]
