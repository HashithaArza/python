# Generated by Django 3.1.7 on 2021-07-07 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0002_delete_mobiledb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specform',
            name='fyi',
        ),
    ]