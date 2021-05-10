# Generated by Django 3.1.7 on 2021-05-07 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignment', '0005_auto_20210507_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='sub_incident_type',
        ),
        migrations.AddField(
            model_name='incident',
            name='type_env',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='incident',
            name='type_inju',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='incident',
            name='type_property',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='incident',
            name='type_vehicle',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incident',
            name='initial_severity',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='incident',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='incident',
            name='reported_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Severity',
        ),
    ]
