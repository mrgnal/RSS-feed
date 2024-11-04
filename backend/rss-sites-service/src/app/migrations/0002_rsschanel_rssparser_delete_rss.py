# Generated by Django 5.1.1 on 2024-10-30 10:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RssChanel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('disable', 'disable')], default='active', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RssParser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('disable', 'disable')], default='active', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField()),
                ('elements', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Rss',
        ),
    ]