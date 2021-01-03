# Generated by Django 2.2.6 on 2020-11-26 06:07

import demoapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('mobile', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='profilephoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(max_length=255, upload_to=demoapp.models.image_path)),
                ('my_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoapp.myprofile')),
            ],
        ),
        migrations.AddField(
            model_name='myprofile',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demoapp.User'),
        ),
    ]