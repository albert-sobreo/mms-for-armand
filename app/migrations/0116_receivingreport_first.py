# Generated by Django 3.2.3 on 2021-07-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0115_auto_20210724_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='receivingreport',
            name='first',
            field=models.BooleanField(default=False, null=True),
        ),
    ]