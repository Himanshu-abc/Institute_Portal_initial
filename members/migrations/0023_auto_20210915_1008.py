# Generated by Django 3.2.6 on 2021-09-15 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0022_alter_syllabus_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]