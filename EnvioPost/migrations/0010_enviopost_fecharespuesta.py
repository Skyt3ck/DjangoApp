# Generated by Django 2.0.6 on 2018-06-09 22:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('EnvioPost', '0009_auto_20180609_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='enviopost',
            name='fechaRespuesta',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 9, 22, 43, 8, 727472, tzinfo=utc)),
        ),
    ]