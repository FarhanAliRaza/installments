# Generated by Django 3.2.8 on 2021-10-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_item_kist'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='ref_phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
