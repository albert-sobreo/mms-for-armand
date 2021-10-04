# Generated by Django 3.2.3 on 2021-07-19 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0109_auto_20210719_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveries',
            name='datetimeVoided',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deliveries',
            name='voided',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='deliveries',
            name='voidedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deVoidedBy', to=settings.AUTH_USER_MODEL),
        ),
    ]
