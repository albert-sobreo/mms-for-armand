# Generated by Django 3.2.3 on 2021-07-31 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0124_poitemsother'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='poItemsOther',
            field=models.ManyToManyField(blank=True, to='app.POItemsOther'),
        ),
    ]