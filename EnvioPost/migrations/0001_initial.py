# Generated by Django 2.0.6 on 2018-06-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='envioPost',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('MRZ', models.TextField()),
                ('hotel', models.CharField(max_length=60)),
                ('app', models.CharField(max_length=20)),
                ('respuesta', models.TextField()),
                ('fechaRespueta', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]