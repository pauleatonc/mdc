# Generated by Django 5.0.2 on 2024-03-02 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_article_title_remove_article_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=3000)),
                ('reference', models.URLField(blank=True, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='articles_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='articles_videos/')),
                ('files', models.FileField(blank=True, null=True, upload_to='articles_files/')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Element', to='posts.article')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
