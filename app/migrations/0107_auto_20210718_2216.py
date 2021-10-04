# Generated by Django 3.2.3 on 2021-07-18 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0106_auto_20210718_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='salescontract',
            name='datetimeVoided',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='voided',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='voidedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='scVoidedBy', to=settings.AUTH_USER_MODEL),
        ),
    ]