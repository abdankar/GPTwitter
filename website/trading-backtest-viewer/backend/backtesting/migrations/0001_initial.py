# Generated by Django 3.2.25 on 2024-06-03 20:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(default=' ', max_length=10)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('close', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='Default strategy description')),
            ],
        ),
        migrations.CreateModel(
            name='BacktestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('ticker', models.CharField(default=' ', max_length=10)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('atr_multiplier', models.FloatField(default=0.0)),
                ('trailing_stop_multiplier', models.FloatField(default=0.0)),
                ('atr_period', models.IntegerField(default=0)),
                ('total_return', models.FloatField(default=0.0)),
                ('portfolio_variance', models.FloatField(default=0.0)),
                ('sharpe_ratio', models.FloatField(default=0.0)),
                ('final_equity', models.FloatField(default=0.0)),
                ('maximum_drawdown', models.FloatField(default=0.0)),
                ('successful_trades', models.IntegerField(default=0)),
                ('minutes_taken', models.IntegerField(default=0)),
                ('sold_at_date', models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 3, 16, 12, 3, 526673))),
                ('score', models.FloatField(default=0.0)),
                ('strategy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='backtest_results', to='backtesting.strategy')),
            ],
        ),
    ]