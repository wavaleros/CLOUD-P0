# Generated by Django 3.1 on 2020-08-12 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_event_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_end_date',
            new_name='event_final_date',
        ),
    ]