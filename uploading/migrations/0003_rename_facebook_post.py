# Generated by Django 3.2 on 2022-03-29 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploading', '0002_rename_image_facebook_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Facebook',
            new_name='Post',
        ),
    ]
