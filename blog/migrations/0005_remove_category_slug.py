# Generated by Django 4.0.1 on 2022-08-24 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
