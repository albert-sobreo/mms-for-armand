# Generated by Django 3.2.3 on 2021-06-29 12:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0068_iiadjusteditems_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('datetimeCreated', models.DateTimeField()),
                ('dateSold', models.DateField()),
                ('amountPaid', models.DecimalField(decimal_places=5, max_digits=18, null=True)),
                ('amountDue', models.DecimalField(decimal_places=5, max_digits=18, null=True)),
                ('amountTotal', models.DecimalField(decimal_places=5, max_digits=18)),
                ('discountPercent', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('discountPeso', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('taxType', models.CharField(blank=True, max_length=20, null=True)),
                ('taxRate', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('taxPeso', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('paymentMethod', models.CharField(max_length=50)),
                ('paymentPeriod', models.CharField(max_length=50)),
                ('chequeNo', models.CharField(blank=True, max_length=50, null=True)),
                ('dueDate', models.DateField(blank=True, null=True)),
                ('bank', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('datetimeApproved', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False, null=True)),
                ('fullyPaid', models.BooleanField(default=False, null=True)),
                ('runningBalance', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('approvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='soApprovedBy', to=settings.AUTH_USER_MODEL)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='soCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('journal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salesorder', to='app.journal')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salesorder', to='app.party')),
                ('quotations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salesorder', to='app.quotations')),
            ],
        ),
        migrations.CreateModel(
            name='SOOtherFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.DecimalField(decimal_places=5, max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=255, null=True)),
                ('salesOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sootherfees', to='app.salesorder')),
            ],
        ),
        migrations.CreateModel(
            name='SOItemsMerch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('cbm', models.CharField(max_length=10, null=True)),
                ('vol', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('pricePerCubic', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('totalCost', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('delivered', models.BooleanField(default=False, null=True)),
                ('merchInventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='soitemsmerch', to='app.merchandiseinventory')),
                ('salesOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='soitemsmerch', to='app.salesorder')),
            ],
        ),
        migrations.CreateModel(
            name='SOatc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountWithheld', models.DecimalField(blank=True, decimal_places=5, max_digits=18, null=True)),
                ('code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='soatc', to='app.atc')),
                ('salesOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='soatc', to='app.salesorder')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='salesOrder',
            field=models.ManyToManyField(blank=True, to='app.SalesOrder'),
        ),
        migrations.AddField(
            model_name='branch',
            name='soOtherFees',
            field=models.ManyToManyField(blank=True, to='app.SOOtherFees'),
        ),
        migrations.AddField(
            model_name='branch',
            name='soatc',
            field=models.ManyToManyField(blank=True, to='app.SOatc'),
        ),
        migrations.AddField(
            model_name='branch',
            name='soitemsMerch',
            field=models.ManyToManyField(blank=True, to='app.SOItemsMerch'),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='salesOrder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salescontract', to='app.salesorder'),
        ),
    ]
