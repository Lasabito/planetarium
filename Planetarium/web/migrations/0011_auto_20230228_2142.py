# Generated by Django 3.2.18 on 2023-02-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_person_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newroommodel',
            name='seats',
            field=models.CharField(default='000000000|00000000000|000000000000|00000000000|0000000', max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='seats',
            field=models.CharField(default='000000000|00000000000|000000000000|00000000000|0000000', max_length=1000),
        ),
    ]
