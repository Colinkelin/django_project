# Generated by Django 4.1.3 on 2022-11-23 08:01

from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.us.models.USStateField(default='NY', max_length=2),
        ),
    ]