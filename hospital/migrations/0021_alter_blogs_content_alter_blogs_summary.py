# Generated by Django 4.0.4 on 2022-07-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_alter_blogs_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='summary',
            field=models.CharField(max_length=1500, null=True),
        ),
    ]
