# Generated by Django 2.2.18 on 2021-02-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_aboutus_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(default='Null', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='role',
            field=models.CharField(default='Null', max_length=50),
            preserve_default=False,
        ),
    ]
