# Generated by Django 3.2.3 on 2021-05-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0005_grades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='final',
            field=models.CharField(blank=True, default='unknown', max_length=10, null=True),
        ),
    ]