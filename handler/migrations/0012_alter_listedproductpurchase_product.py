# Generated by Django 4.1.2 on 2024-08-31 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("handler", "0011_listedproductpurchase"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listedproductpurchase",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="handler.listedproduct"
            ),
        ),
    ]
