# Generated by Django 4.1.3 on 2022-11-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_listing_transmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='engine',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='listing',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default=None, max_length=20),
        ),
    ]
