# Generated by Django 4.2.14 on 2024-08-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_card_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="color",
            field=models.CharField(max_length=20, verbose_name="color"),
        ),
    ]
