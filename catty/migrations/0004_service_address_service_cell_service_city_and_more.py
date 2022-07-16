# Generated by Django 4.0.6 on 2022-07-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catty', '0003_remove_service_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='cell',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='service',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='url',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='service',
            name='zipcode',
            field=models.CharField(default='', max_length=5),
        ),
    ]
