# Generated by Django 2.2.6 on 2020-11-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.IntegerField(null=True),
        ),
    ]
