# Generated by Django 3.2.18 on 2023-02-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_newroommodel_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='newroommodel',
            name='duration',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
