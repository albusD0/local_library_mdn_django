# Generated by Django 5.0.6 on 2024-06-28 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.TextField(blank=True, null=True),
        ),
    ]
