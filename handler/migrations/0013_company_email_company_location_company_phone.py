# Generated by Django 4.1.2 on 2024-08-31 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("handler", "0012_alter_listedproductpurchase_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="email",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="company",
            name="location",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="company",
            name="phone",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
