# Generated by Django 3.2.3 on 2021-09-24 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0163_auto_20210924_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchdefaultchildaccount',
            name='rm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='branchdefaultrm', to='app.accountchild'),
        ),
        migrations.AddField(
            model_name='completionreport',
            name='datetimeApproved',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]