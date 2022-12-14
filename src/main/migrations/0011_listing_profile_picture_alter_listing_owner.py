# Generated by Django 4.1.3 on 2022-11-27 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_photo'),
        ('main', '0010_rename_seller_listing_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='main/pics'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='users.profile'),
        ),
    ]
