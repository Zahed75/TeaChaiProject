# Generated by Django 3.2 on 2021-07-26 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tea_App', '0025_auto_20210726_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 26, 23, 24, 26, 326056)),
        ),
    ]