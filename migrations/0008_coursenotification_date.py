# Generated by Django 3.2.3 on 2021-06-02 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0007_coursenotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursenotification',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
