# Generated by Django 3.2.3 on 2021-09-24 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0162_auto_20210924_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='CRSpareParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='crspareparts', to='app.completionreport')),
                ('receivingReport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='crspareparts', to='app.receivingreport')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='crSpareParts',
            field=models.ManyToManyField(blank=True, to='app.CRSpareParts'),
        ),
    ]
