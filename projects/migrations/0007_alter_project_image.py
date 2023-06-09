# Generated by Django 4.1.8 on 2023-05-04 12:09

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='projects/default.png', upload_to='projects/', validators=[projects.models.Project.validate_image]),
        ),
    ]
