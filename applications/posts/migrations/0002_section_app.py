# Generated by Django 5.0.2 on 2024-02-29 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('sitecomponents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='app',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='sitecomponents.app'),
        ),
    ]
