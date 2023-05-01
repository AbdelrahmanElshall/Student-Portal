# Generated by Django 3.2.3 on 2021-05-27 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0003_auto_20210521_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('file_link', models.CharField(blank=True, max_length=200, null=True)),
                ('department', models.CharField(blank=True, default='computer', max_length=200, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollments.course')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='enrollments.doctor')),
            ],
        ),
    ]