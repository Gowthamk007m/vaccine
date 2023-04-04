# Generated by Django 4.1.5 on 2023-03-09 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pediatric_clinic', '0004_available_date_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pediatric_clinic.available_date'),
        ),
    ]