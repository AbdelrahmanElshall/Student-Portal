# Generated by Django 3.2.3 on 2021-06-02 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0006_alter_grades_final'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(blank=True, max_length=400, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollments.course')),
            ],
        ),
    ]
