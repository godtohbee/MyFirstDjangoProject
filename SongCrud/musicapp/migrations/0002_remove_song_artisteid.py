# Generated by Django 4.1.2 on 2022-10-28 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artisteId',
        ),
    ]
