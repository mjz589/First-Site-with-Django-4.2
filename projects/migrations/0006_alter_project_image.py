# Generated by Django 4.1.8 on 2023-05-04 11:52

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_project_summary_project_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='projects/single_project.png', upload_to='projects/', validators=[projects.models.Project.validate_image]),
        ),
    ]
