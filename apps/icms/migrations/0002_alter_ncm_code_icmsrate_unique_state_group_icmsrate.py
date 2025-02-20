# Generated by Django 4.2.14 on 2024-12-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("icms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ncm",
            name="code",
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AddConstraint(
            model_name="icmsrate",
            constraint=models.UniqueConstraint(
                fields=("state", "group"), name="unique_state_group_icmsrate"
            ),
        ),
    ]
