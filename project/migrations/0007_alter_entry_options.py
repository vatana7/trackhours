# Generated by Django 3.2.3 on 2021-06-07 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_entry_is_tracked'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created_at']},
        ),
    ]
