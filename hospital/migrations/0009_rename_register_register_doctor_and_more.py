# Generated by Django 4.0.4 on 2022-07-25 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_register_delete_register_doctor_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register',
            new_name='register_doctor',
        ),
        migrations.AlterModelTable(
            name='register_doctor',
            table='register_doctor',
        ),
    ]
