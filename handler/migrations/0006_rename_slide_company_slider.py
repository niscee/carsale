# Generated by Django 4.1.2 on 2024-08-20 13:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("handler", "0005_company_slide"),
    ]

    operations = [
        migrations.RenameField(
            model_name="company",
            old_name="slide",
            new_name="slider",
        ),
    ]
