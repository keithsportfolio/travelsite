# Generated by Django 2.2.4 on 2022-06-18 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelsiteapp', '0006_auto_20220618_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continent',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='continent', to='travelsiteapp.Trip'),
        ),
    ]