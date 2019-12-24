# Generated by Django 3.0 on 2019-12-23 22:06

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0018_auto_20191223_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
