# Generated by Django 2.2.4 on 2019-10-15 05:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0004_auto_20191008_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='applicants',
            field=models.ManyToManyField(related_name='applicants', to=settings.AUTH_USER_MODEL),
        ),
    ]
