# Generated by Django 2.2 on 2020-10-03 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_auto_20201003_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terminfo',
            name='current_week',
        ),
    ]
