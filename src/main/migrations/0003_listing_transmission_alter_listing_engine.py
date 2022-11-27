# Generated by Django 4.1.3 on 2022-11-26 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_listing_brand_listing_color_listing_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='listing',
            name='engine',
            field=models.CharField(max_length=20),
        ),
    ]