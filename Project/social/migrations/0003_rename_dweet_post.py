# Generated by Django 4.0.4 on 2022-05-28 13:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0002_dweet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dweet',
            new_name='Post',
        ),
    ]
