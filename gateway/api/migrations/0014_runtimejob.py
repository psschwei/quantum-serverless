# Generated by Django 4.2.2 on 2024-01-20 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_program_groups_catalogentry"),
    ]

    operations = [
        migrations.CreateModel(
            name="RuntimeJob",
            fields=[
                (
                    "runtime_job",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "job",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.job",
                    ),
                ),
            ],
        ),
    ]