# Generated by Django 4.1.8 on 2023-04-16 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jobs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=255)),
                ("body", models.TextField()),
                ("responsibilities", models.TextField()),
                ("requirement", models.TextField()),
                ("publish", models.DateTimeField(default=django.utils.timezone.now)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.CharField(max_length=250)),
            ],
            options={
                "verbose_name": "job",
                "verbose_name_plural": "Jobs",
                "ordering": ["-publish"],
            },
        ),
    ]