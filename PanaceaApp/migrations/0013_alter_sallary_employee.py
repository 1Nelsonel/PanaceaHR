# Generated by Django 4.0.8 on 2022-11-28 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PanaceaApp', '0012_remove_sallary_nhif_remove_sallary_nssf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sallary',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PanaceaApp.employee'),
        ),
    ]
