# Generated by Django 4.2 on 2024-06-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_slider_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='mobile_image',
            field=models.ImageField(blank=True, null=True, upload_to='SliderMobile/'),
        ),
    ]
