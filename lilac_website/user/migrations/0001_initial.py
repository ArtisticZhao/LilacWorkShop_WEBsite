# Generated by Django 2.2.4 on 2019-09-24 03:33

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50)),
                ('school_emails', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': '参与学校',
                'verbose_name_plural': '参与学校',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('TE', '项目发布者'), ('ST', '项目参与者')], default='ST', max_length=2)),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/%Y%m%d/')),
                ('body', ckeditor.fields.RichTextField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school', to='user.School')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
