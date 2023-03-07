# Generated by Django 3.2.18 on 2023-02-18 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_newroommodel_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newroommodel',
            name='info',
        ),
        migrations.AddField(
            model_name='newroommodel',
            name='heading',
            field=models.TextField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]