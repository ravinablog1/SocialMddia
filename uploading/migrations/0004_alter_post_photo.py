# Generated by Django 3.2 on 2022-04-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploading', '0003_rename_facebook_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='\\photo'),
        ),
    ]