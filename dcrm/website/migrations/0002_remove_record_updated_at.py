# Generated by Django 5.1.4 on 2025-01-03 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='updated_at',
        ),
    ]
