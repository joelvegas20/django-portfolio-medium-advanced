# Generated by Django 4.1.5 on 2023-01-16 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_link_alter_project_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created'], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
    ]
