# Generated by Django 4.2.14 on 2024-12-18 17:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("icms", "0002_alter_ncm_code_icmsrate_unique_state_group_icmsrate"),
        ("margin", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("contract_id", models.BigIntegerField()),
                ("contract_number", models.CharField(max_length=10)),
                ("client_name", models.CharField(max_length=255)),
                ("client_id", models.BigIntegerField()),
                ("construction_name", models.CharField(max_length=255)),
                ("delivery_date", models.DateField()),
                ("net_cost", models.FloatField()),
                ("net_cost_without_taxes", models.FloatField()),
                ("net_cost_with_margin", models.FloatField(blank=True, null=True)),
                ("freight_value", models.FloatField()),
                ("commission", models.FloatField()),
                ("other_taxes", models.FloatField()),
                ("account", models.IntegerField()),
                ("installments", models.IntegerField()),
                ("xped", models.CharField(max_length=255)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="margin.company",
                    ),
                ),
                (
                    "icms",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="icms.icmsrate",
                    ),
                ),
                (
                    "margin",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="margin.percentage",
                    ),
                ),
                (
                    "ncm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="icms.ncm",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="icms.state",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ContractItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("index", models.PositiveIntegerField()),
                ("name", models.CharField(max_length=255)),
                ("contribution_rate", models.FloatField()),
                ("sale_item_id", models.BigIntegerField()),
                ("quantity", models.PositiveIntegerField()),
                ("product_id", models.BigIntegerField()),
                ("updated_value", models.FloatField(blank=True, null=True)),
                (
                    "contract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="margin.contract",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]