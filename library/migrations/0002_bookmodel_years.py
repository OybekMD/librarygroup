# Generated by Django 4.2.3 on 2023-07-18 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='years',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
