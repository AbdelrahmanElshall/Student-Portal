# Generated by Django 3.2.3 on 2021-05-21 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0002_rename_course_id_teching_course_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='doc_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_name',
            new_name='name',
        ),
    ]
