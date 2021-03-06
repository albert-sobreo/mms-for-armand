# Generated by Django 3.2.3 on 2021-09-22 07:26

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0158_testuploadfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletionReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('datetimeCreated', models.DateTimeField()),
                ('reportDate', models.DateField(blank=True, null=True)),
                ('malfuncDate', models.DateField(blank=True, null=True)),
                ('damageDescription', models.TextField(blank=True, null=True)),
                ('damagePhoto', models.ImageField(blank=True, null=True, upload_to='cr/damage/')),
                ('recommendation', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('successPhoto', models.ImageField(blank=True, null=True, upload_to='cr/success/')),
                ('ppe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.ppe')),
                ('spareParts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.receivingreport')),
            ],
        ),
        migrations.CreateModel(
            name='CRVendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentAmount', models.DecimalField(decimal_places=5, default=Decimal('0'), max_digits=20)),
                ('cr', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.completionreport')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.party')),
            ],
        ),
    ]
