# Generated by Django 3.0.5 on 2020-04-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteback', '0003_auto_20200421_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]