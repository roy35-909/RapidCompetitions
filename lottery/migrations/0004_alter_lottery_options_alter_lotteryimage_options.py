# Generated by Django 4.2 on 2024-06-11 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0003_alter_lottery_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lottery',
            options={'verbose_name': 'Competition', 'verbose_name_plural': 'Competitions'},
        ),
        migrations.AlterModelOptions(
            name='lotteryimage',
            options={'verbose_name': 'CompetitionImage', 'verbose_name_plural': 'CompetitionImages'},
        ),
    ]
