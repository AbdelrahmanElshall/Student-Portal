# Generated by Django 3.2.3 on 2021-05-21 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enrollments', '0003_auto_20210521_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=4, max_digits=5)),
                ('hours', models.IntegerField()),
                ('level', models.CharField(max_length=50)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollments.student')),
            ],
            options={
                'ordering': ['gpa'],
            },
        ),
    ]
