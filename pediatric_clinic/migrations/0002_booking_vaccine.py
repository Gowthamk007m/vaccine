# Generated by Django 4.1.5 on 2023-03-08 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pediatric_clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='vaccine',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
