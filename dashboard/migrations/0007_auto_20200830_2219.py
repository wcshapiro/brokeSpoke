# Generated by Django 3.0.4 on 2020-08-31 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_timelogs_paymentstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(blank=True, default='NULL', max_length=80),
        ),
        migrations.AlterField(
            model_name='users',
            name='emergencyName',
            field=models.CharField(blank=True, default='NULL', max_length=40),
        ),
    ]