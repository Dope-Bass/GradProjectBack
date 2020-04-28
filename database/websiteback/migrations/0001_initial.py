# Generated by Django 3.0.5 on 2020-04-18 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('founder', models.CharField(max_length=120)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('check_date', models.DateField()),
                ('design', models.BooleanField()),
                ('functional', models.BooleanField()),
                ('discussion', models.BooleanField()),
                ('idea', models.BooleanField()),
                ('bug', models.BooleanField()),
                ('not_formal', models.BooleanField()),
                ('description', models.TextField()),
            ],
        ),
    ]