# Generated by Django 3.2.3 on 2021-06-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0071_auto_20210629_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='wep',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='quotations',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quotations',
            name='wep',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='receivingreport',
            name='wep',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='wep',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='wep',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
    ]
