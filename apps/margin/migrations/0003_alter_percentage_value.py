# Generated by Django 4.2.14 on 2025-01-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("margin", "0002_contract_contractitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="percentage",
            name="value",
            field=models.DecimalField(decimal_places=2, max_digits=5, unique=True),
        ),
    ]
