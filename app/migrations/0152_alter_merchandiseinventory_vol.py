# Generated by Django 3.2.3 on 2021-09-17 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0151_alter_merchandiseinventory_vol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandiseinventory',
            name='vol',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
    ]