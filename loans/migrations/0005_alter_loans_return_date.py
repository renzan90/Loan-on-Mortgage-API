# Generated by Django 5.0.7 on 2024-09-29 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0004_alter_loans_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='return_date',
            field=models.DateField(default=datetime.date(2025, 9, 29)),
        ),
    ]
