# Generated by Django 3.2 on 2022-03-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_post', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
