# Generated by Django 4.2.2 on 2023-06-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='geolocation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='holiday',
            field=models.TextField(blank=True, null=True),
        ),
    ]
