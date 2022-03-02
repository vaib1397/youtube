# Generated by Django 4.0.2 on 2022-02-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIVideos',
            fields=[
                ('video_id', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('channel_id', models.CharField(blank=True, max_length=55, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
