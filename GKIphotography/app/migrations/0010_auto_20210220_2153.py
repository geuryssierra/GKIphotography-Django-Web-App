# Generated by Django 2.2.18 on 2021-02-21 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_photocollection_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('coverImage', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AlterField(
            model_name='photocollection',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
    ]
