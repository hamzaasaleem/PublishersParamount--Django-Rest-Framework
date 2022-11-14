# Generated by Django 4.1.2 on 2022-11-14 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_reviewer_journal_alter_author_user_image_and_more'),
        ('manuscripts', '0009_manurev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manurev',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
        migrations.CreateModel(
            name='ManuEditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.editor')),
                ('manuscript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.manuscript')),
            ],
        ),
    ]
