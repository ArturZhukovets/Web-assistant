# Generated by Django 4.0.3 on 2022-07-19 22:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0002_alter_url_source_url_alter_url_url_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='source_url',
            field=models.CharField(max_length=500, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]
