# Generated by Django 4.2.14 on 2024-07-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green', '0006_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video_url',
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
