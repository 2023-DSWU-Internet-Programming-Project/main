# Generated by Django 4.2.7 on 2023-11-22 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("message", "0009_alter_comment_askpost_alter_comment_findpost"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="completePost",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="message.completeitem",
            ),
        ),
    ]