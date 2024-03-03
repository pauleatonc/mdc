# Generated by Django 5.0.2 on 2024-03-02 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_section_orden_subsection_orden_title_orden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.RemoveField(
            model_name='article',
            name='description',
        ),
        migrations.RemoveField(
            model_name='article',
            name='files',
        ),
        migrations.RemoveField(
            model_name='article',
            name='images',
        ),
        migrations.RemoveField(
            model_name='article',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='article',
            name='video',
        ),
        migrations.AddField(
            model_name='article',
            name='orden',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='subsection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='posts.subsection'),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=3000)),
                ('reference', models.URLField(blank=True, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='articles_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='articles_videos/')),
                ('files', models.FileField(blank=True, null=True, upload_to='articles_files/')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='posts.article')),
            ],
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]
