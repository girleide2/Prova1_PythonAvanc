# Generated by Django 5.0.6 on 2024-05-10 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produto",
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
                ("text", models.CharField(max_length=200)),
                ("data_add", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Promocao",
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
                ("data_inicio", models.CharField(max_length=50)),
                ("data_fim", models.CharField(max_length=50)),
                ("valor", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Promoções",
            },
        ),
        migrations.CreateModel(
            name="Detalhe",
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
                ("detalhe", models.TextField()),
                ("data_add", models.DateTimeField(auto_now_add=True)),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tygra_app.produto",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="produto",
            name="promocao",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tygra_app.promocao",
            ),
        ),
    ]
