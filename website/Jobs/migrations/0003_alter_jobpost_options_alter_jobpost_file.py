# Generated by Django 4.1.8 on 2023-04-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0002_alter_jobs_status_jobpost"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="jobpost",
            options={"verbose_name": "job Cv"},
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="file",
            field=models.FileField(upload_to=""),
        ),
    ]
