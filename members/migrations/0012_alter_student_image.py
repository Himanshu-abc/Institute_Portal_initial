# Generated by Django 3.2.6 on 2021-09-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_alter_news_gallery_news_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile/'),
        ),
    ]