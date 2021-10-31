# Generated by Django 3.2.4 on 2021-06-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_plan_months'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_rcvd', models.PositiveIntegerField(blank=True, null=True)),
                ('total_pending', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]