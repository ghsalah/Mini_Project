# Generated by Django 5.1.1 on 2024-09-22 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_1', '0002_imagepost_dummy_field'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobPost',
        ),
        migrations.RemoveField(
            model_name='imagepost',
            name='dummy_field',
        ),
    ]
