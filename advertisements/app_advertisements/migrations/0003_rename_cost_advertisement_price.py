# Generated by Django 4.2.5 on 2023-09-20 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='cost',
            new_name='price',
        ),
    ]