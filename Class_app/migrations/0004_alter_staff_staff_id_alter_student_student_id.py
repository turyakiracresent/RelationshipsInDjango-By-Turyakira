# Generated by Django 5.2.4 on 2025-07-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Class_app', '0003_remove_staff_id_remove_student_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Staff_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
