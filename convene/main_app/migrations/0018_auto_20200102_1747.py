# Generated by Django 2.2.6 on 2020-01-02 17:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_auto_20191223_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 2, 17, 47, 3, 313225, tzinfo=utc)),
        ),
    ]
