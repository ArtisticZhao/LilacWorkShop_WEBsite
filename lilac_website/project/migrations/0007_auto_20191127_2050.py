# Generated by Django 2.2.4 on 2019-11-27 12:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20191127_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='applicants',
            field=models.ManyToManyField(blank=True, related_name='applicants', to=settings.AUTH_USER_MODEL),
        ),
    ]
