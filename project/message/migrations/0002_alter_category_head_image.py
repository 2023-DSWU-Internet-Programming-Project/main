# Generated by Django 4.2.7 on 2023-11-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("message", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="head_image",
            field=models.ImageField(blank=True, upload_to="message/images/category/"),
        ),
    ]
