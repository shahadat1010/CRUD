# Generated by Django 4.1.6 on 2023-02-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("APP", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=200)),
                ("news_details", models.TextField()),
            ],
        ),
        migrations.DeleteModel(name="Employees",),
    ]
