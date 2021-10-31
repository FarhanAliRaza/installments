# Generated by Django 3.2.4 on 2021-06-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imei',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='net_rate',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='qty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
