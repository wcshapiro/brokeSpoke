# Generated by Django 3.0.4 on 2020-07-30 20:40

import django.contrib.postgres.fields.citext
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200726_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='firstname',
            field=django.contrib.postgres.fields.citext.CICharField(default='NULL', max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastname',
            field=django.contrib.postgres.fields.citext.CICharField(default='NULL', max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='middlename',
            field=django.contrib.postgres.fields.citext.CICharField(default='NULL', max_length=40),
        ),
    ]
