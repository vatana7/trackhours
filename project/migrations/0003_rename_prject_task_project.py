# Generated by Django 3.2.3 on 2021-06-04 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='prject',
            new_name='project',
        ),
    ]
