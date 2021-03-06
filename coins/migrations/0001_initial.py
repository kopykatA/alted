# Generated by Django 2.0 on 2018-04-23 17:09

import alted.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('code', models.CharField(max_length=8, unique=True)),
                ('fiat', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=32, unique=True)),
                ('price_usd', models.DecimalField(blank=True, decimal_places=8, max_digits=16, null=True)),
                ('price_btc', models.DecimalField(blank=True, decimal_places=8, max_digits=16, null=True)),
                ('volume_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True)),
                ('volume_btc', models.DecimalField(blank=True, decimal_places=8, max_digits=32, null=True)),
                ('tethered_fiat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coins.Coin')),
            ],
            bases=(models.Model, alted.utils.SlugifyMixin),
        ),
        migrations.CreateModel(
            name='Tick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price_usd', models.DecimalField(decimal_places=8, max_digits=32)),
                ('price_btc', models.DecimalField(decimal_places=8, max_digits=32)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.Coin')),
            ],
        ),
    ]
