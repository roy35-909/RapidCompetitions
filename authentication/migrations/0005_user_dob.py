# Generated by Django 4.2 on 2024-07-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_checkout_payment_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
