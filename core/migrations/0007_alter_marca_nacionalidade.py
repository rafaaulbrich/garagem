# Generated by Django 5.0.6 on 2024-08-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_marca"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marca",
            name="nacionalidade",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
