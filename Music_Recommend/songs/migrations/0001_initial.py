# Generated by Django 4.1.3 on 2022-11-03 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
            options={
                'db_table': 'song',
            },
        ),
    ]
