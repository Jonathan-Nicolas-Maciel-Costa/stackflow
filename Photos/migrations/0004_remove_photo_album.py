# Generated by Django 4.2.1 on 2023-06-02 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Photos', '0003_alter_photo_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='album',
        ),
    ]
