# Generated by Django 3.1.2 on 2020-11-02 17:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20201102_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='neighbourhood_logo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
