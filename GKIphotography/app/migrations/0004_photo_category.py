# Generated by Django 2.2.18 on 2021-02-20 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_photo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.CharField(default='No Category', max_length=50),
            preserve_default=False,
        ),
    ]