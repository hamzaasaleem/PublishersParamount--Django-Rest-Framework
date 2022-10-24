# Generated by Django 4.1.2 on 2022-10-23 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0002_remove_manuscript_user_manuscript_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manuscript',
            old_name='description',
            new_name='abstract',
        ),
        migrations.AddField(
            model_name='manuscript',
            name='article_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='manuscript',
            name='keywords',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='manuscript',
            name='status',
            field=models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('minor', 'Minor'), ('major', 'Major'), ('none', 'None')], default='none', max_length=50),
        ),
    ]