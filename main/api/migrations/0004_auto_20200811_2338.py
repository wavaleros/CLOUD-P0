# Generated by Django 3.1 on 2020-08-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200811_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnail'),
        ),
    ]