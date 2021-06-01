# Generated by Django 3.2.3 on 2021-06-01 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=10),
        ),
    ]
