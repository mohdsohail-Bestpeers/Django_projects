# Generated by Django 2.2.6 on 2020-12-01 06:00

from django.db import migrations, models
import django.db.models.deletion
import formapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('wedding', 'Wedding'), ('birthday', 'BirthDay'), ('stage_decoration', 'Stage_Decoration')], default='birthday', max_length=50)),
                ('Max_Guest', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='event_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(max_length=255, upload_to=formapp.models.image_path)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_photos', to='formapp.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formapp.User'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('indore', 'Indore'), ('ujjain', 'Ujjain'), ('pune', 'Pune'), ('mumbai', 'Mumbai'), ('banglore', 'Banglore'), ('other', 'Other')], default='indore', max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formapp.Event')),
            ],
        ),
    ]
