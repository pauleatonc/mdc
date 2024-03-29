# Generated by Django 5.0.2 on 2024-03-03 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_element_title_element_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='reference',
            field=models.URLField(blank=True, null=True),
        ),
    ]
