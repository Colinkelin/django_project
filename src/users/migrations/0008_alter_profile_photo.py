# Generated by Django 4.1.3 on 2022-11-27 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='', upload_to='main/pics'),
            preserve_default=False,
        ),
    ]
