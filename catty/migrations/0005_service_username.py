# Generated by Django 4.0.6 on 2022-07-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catty', '0004_service_address_service_cell_service_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='username',
            field=models.CharField(default='unknown_user', max_length=100),
        ),
    ]
