# Generated by Django 3.2.3 on 2021-05-16 00:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('phone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=200)),
                ('subTo', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
