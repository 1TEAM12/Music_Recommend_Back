# Generated by Django 4.1.3 on 2022-11-07 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=70)),
                ('rank', models.CharField(blank=True, max_length=70)),
                ('title', models.CharField(blank=True, max_length=70)),
                ('genre', models.CharField(blank=True, max_length=70)),
                ('singer', models.CharField(blank=True, max_length=70)),
                ('type', models.CharField(blank=True, max_length=70)),
                ('lyrics', models.TextField(blank=True)),
                ('likes', models.IntegerField(blank=True)),
                ('image', models.TextField(blank=True)),
                ('genre_no', models.IntegerField(blank=True)),
                ('youtube_url', models.TextField(blank=True)),
                ('song_likes', models.ManyToManyField(blank=True, related_name='like_song', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'song',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recode', models.FileField(upload_to='voice_record')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voices', to='songs.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voice_likes', models.ManyToManyField(blank=True, related_name='like_voice', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'voice',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='songs.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment',
                'ordering': ['-created_at'],
            },
        ),
    ]
