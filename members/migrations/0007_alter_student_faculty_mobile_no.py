# Generated by Django 3.2.6 on 2021-08-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_student_faculty_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_faculty',
            name='mobile_no',
            field=models.CharField(max_length=14),
        ),
    ]