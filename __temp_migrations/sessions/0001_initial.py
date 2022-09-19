# Generated by Django 2.2.12 on 2022-09-19 15:02

import django.contrib.sessions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='session key')),
                ('session_data', models.TextField(verbose_name='session data')),
                ('expire_date', models.DateTimeField(db_index=True, verbose_name='expire date')),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
                'db_table': 'django_session',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.sessions.models.SessionManager()),
            ],
        ),
    ]
