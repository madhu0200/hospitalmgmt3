# Generated by Django 4.0.4 on 2022-07-28 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_alter_blogs_content_alter_blogs_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=25, null=True)),
                ('doctor_name', models.CharField(max_length=25, null=True)),
                ('required_speciality', models.CharField(max_length=25, null=True)),
                ('appointment_date', models.DateField(default=datetime.date)),
                ('appointment_time', models.TimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='blogs',
            name='category',
            field=models.CharField(choices=[('Mental health', 'Mental health'), ('covid 19', 'covid 19'), ('heart disease', 'heart disease'), ('immunization', 'immunization')], max_length=25),
        ),
    ]
