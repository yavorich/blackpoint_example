# Generated by Django 5.1.3 on 2024-11-14 13:34

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_subscriptiontariff_delete_basesubscription_and_more'),
        ('vending', '0002_place_tariffs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='tariffs',
            field=models.ManyToManyField(blank=True, default=django.db.models.manager.BaseManager.all, related_name='places', to='account.subscriptiontariff'),
        ),
    ]
