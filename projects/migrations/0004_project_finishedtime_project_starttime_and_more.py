# Generated by Django 4.1.8 on 2023-05-03 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='FinishedTime',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='project',
            name='StartTime',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='project',
            name='customer',
            field=models.CharField(default='unknown', max_length=120),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]