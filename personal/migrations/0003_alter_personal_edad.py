# Generated by Django 4.0 on 2022-09-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_rename_tecnologia_personal_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='edad',
            field=models.IntegerField(default=0),
        ),
    ]