# Generated by Django 4.2 on 2024-06-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0004_alter_lottery_options_alter_lotteryimage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottery',
            name='have_any_cash_alternative',
            field=models.BooleanField(default=False),
        ),
    ]
