# Generated by Django 3.2.18 on 2023-02-19 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_newroommodel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newroommodel',
            name='heading',
            field=models.CharField(max_length=45),
        ),
    ]