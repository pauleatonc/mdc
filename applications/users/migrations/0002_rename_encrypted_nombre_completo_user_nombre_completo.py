# Generated by Django 4.2.2 on 2024-06-20 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='encrypted_nombre_completo',
            new_name='nombre_completo',
        ),
    ]