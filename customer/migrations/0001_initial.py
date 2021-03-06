# Generated by Django 3.2.4 on 2021-06-22 13:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('ref_name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('adress', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='none', max_length=200)),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('total', models.PositiveIntegerField(blank=True, null=True)),
                ('recieved', models.PositiveIntegerField(blank=True, null=True)),
                ('pending', models.PositiveIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('months', models.ManyToManyField(to='customer.Month')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=255, null=True)),
                ('total_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('total_recieved', models.PositiveIntegerField(blank=True, null=True)),
                ('total_pending', models.PositiveIntegerField(blank=True, null=True)),
                ('total_kist_months', models.CharField(choices=[('6', '6'), ('10', '10')], default='6', max_length=3)),
                ('advance_taken', models.PositiveIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer')),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.plan')),
            ],
        ),
    ]
