# Generated by Django 3.1.7 on 2021-04-16 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Epic',
            new_name='epic',
        ),
    ]
