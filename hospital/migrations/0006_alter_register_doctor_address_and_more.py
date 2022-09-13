# Generated by Django 4.0.4 on 2022-07-25 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_alter_register_doctor_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_doctor',
            name='address',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='register_patient',
            name='address',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='register_patient',
            name='profile_pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
