# Generated by Django 2.2.4 on 2019-08-26 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Token',
        ),
    ]
