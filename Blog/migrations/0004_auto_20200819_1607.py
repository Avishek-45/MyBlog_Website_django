# Generated by Django 3.0.8 on 2020-08-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_blog_short_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(blank=True),
        ),
    ]
