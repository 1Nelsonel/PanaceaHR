# Generated by Django 4.1.3 on 2022-11-21 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PanaceaApp', '0011_alter_sallary_options_sallary_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sallary',
            name='nhif',
        ),
        migrations.RemoveField(
            model_name='sallary',
            name='nssf',
        ),
    ]
