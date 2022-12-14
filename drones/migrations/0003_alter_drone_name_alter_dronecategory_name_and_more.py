# Generated by Django 4.1 on 2022-08-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0002_pilot_competition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='dronecategory',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
