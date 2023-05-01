# Generated by Django 3.2.3 on 2021-05-16 04:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_auto_20210516_0602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formmodel',
            options={'ordering': ['done', '-date']},
        ),
        migrations.AddField(
            model_name='formmodel',
            name='adminComments',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
