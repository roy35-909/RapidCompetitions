# Generated by Django 4.2 on 2024-06-30 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_winner_winner_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lotteryticket',
            options={'verbose_name': 'Competition Ticket', 'verbose_name_plural': 'Competition Tickets'},
        ),
    ]
