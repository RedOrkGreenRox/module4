# Generated by Django 4.2.5 on 2023-09-22 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0003_rename_cost_advertisement_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
