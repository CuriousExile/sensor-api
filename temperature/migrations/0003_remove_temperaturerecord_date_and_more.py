# Generated by Django 4.2.6 on 2023-10-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0002_temperaturerecord_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temperaturerecord',
            name='date',
        ),
        migrations.AddField(
            model_name='temperaturerecord',
            name='sourceName',
            field=models.CharField(default='unknown', max_length=255),
        ),
    ]