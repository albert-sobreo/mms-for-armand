# Generated by Django 3.2.3 on 2021-06-28 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_auto_20210628_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iiadjusteditems',
            old_name='barcode',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='iiitemsmerch',
            old_name='barcode',
            new_name='code',
        ),
        migrations.RemoveField(
            model_name='iiitemsmerch',
            name='remaining',
        ),
    ]
