# Generated by Django 5.1.2 on 2024-11-09 16:13

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100, verbose_name='Type')),
                ('price', models.FloatField(default=0)),
                ('expire_time', models.IntegerField(default=30, help_text='Expiration time in days')),
                ('max_feeds', models.IntegerField(default=0, help_text='Maximum number of feeds')),
                ('max_rss', models.IntegerField(default=0, help_text='Maximum number of RSS sources')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('beginning_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.UUIDField(default=uuid.uuid4)),
                ('subscription_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='subscriptions.subscriptiontype')),
            ],
        ),
    ]
