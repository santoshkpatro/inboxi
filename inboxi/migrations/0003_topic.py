# Generated by Django 5.0.2 on 2024-02-19 19:41

import django.contrib.postgres.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inboxi", "0002_subscriber"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=124, unique=True)),
                (
                    "tags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=124),
                        default=list,
                        size=None,
                    ),
                ),
                ("is_public", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("subscriber_count", models.BigIntegerField(default=0)),
            ],
            options={
                "db_table": "topics",
            },
        ),
    ]
