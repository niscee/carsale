# Generated by Django 4.1.2 on 2024-08-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("handler", "0002_category_product_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("message", models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="availability",
            field=models.BooleanField(default=True),
        ),
    ]
