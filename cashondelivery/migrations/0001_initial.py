# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cashondelivery.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CashOnDeliveryTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('order_number', models.CharField(max_length=128)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(null=True,
                                               max_digits=12, decimal_places=2, blank=True)),
                ('currency', models.CharField(max_length=8, null=True, blank=True)),
                ('reference', models.CharField(
                    default=cashondelivery.models._make_uuid, unique=True, max_length=100, blank=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('date_confirmed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
