# Generated by Django 3.2.5 on 2022-12-18 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patientmaneger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='dob',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]
