# Generated by Django 2.2.4 on 2019-09-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='is_project',
            field=models.BooleanField(default=True, verbose_name='是否在项目页可见'),
        ),
    ]