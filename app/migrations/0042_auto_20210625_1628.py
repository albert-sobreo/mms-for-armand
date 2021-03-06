# Generated by Django 3.2.3 on 2021-06-25 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20210625_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salescontract',
            name='bank',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salescontract',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salescontract',
            name='taxPeso',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
    ]
