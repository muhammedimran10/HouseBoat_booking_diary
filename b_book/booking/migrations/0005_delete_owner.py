# Generated by Django 4.2.3 on 2023-08-01 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Owner',
        ),
    ]