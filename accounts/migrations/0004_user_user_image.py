# Generated by Django 4.1.2 on 2022-10-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_user_image_author_user_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='user_image/'),
        ),
    ]
