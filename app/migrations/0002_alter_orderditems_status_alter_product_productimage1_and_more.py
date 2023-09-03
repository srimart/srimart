# Generated by Django 4.2.3 on 2023-09-03 16:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderditems',
            name='status',
            field=models.CharField(choices=[('On the Way', 'On the way'), ('Packed', 'Packed'), ('cancel', 'cancel'), ('Deliverd', 'Deliverd'), ('ACCEPTED', 'ACCEPTED')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='productimage1',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productimage2',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productimage3',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productimage4',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
    ]