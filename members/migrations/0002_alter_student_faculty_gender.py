# Generated by Django 3.2.6 on 2021-08-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_faculty',
            name='Gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('other', 'other')], max_length=6),
        ),
    ]
