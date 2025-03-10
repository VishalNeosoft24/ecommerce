# Generated by Django 4.2.14 on 2024-10-21 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_panel', '0021_delete_orderstatuslogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEventTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=255)),
                ('event_time', models.DateTimeField(auto_now_add=True)),
                ('event_metadata', models.JSONField(blank=True, null=True)),
                ('session_id', models.CharField(blank=True, max_length=255, null=True)),
                ('ip_address', models.CharField(max_length=45)),
                ('device_type', models.CharField(max_length=100)),
                ('browser_info', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_event', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
