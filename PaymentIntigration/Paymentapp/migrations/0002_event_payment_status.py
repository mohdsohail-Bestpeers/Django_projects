# Generated by Django 2.2.6 on 2020-12-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paymentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='payment_status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]