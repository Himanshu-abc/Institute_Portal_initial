# Generated by Django 3.2.6 on 2021-08-23 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_student_faculty_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_faculty',
            name='Gender',
            field=models.CharField(choices=[('other', 'other'), ('Female', 'Female'), ('Male', 'Male')], max_length=6),
        ),
    ]
