# Generated by Django 2.2.4 on 2022-10-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsiteapp', '0008_auto_20220618_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='photo_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
