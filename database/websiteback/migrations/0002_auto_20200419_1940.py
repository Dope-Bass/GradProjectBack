# Generated by Django 3.0.5 on 2020-04-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
