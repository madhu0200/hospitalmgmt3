# Generated by Django 4.0.4 on 2022-07-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_alter_register_doctor_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_doctor',
            name='profile_pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
