# Generated by Django 3.1.7 on 2021-05-07 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0004_auto_20210507_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='sub_incident_type',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='IncidentType',
        ),
    ]
