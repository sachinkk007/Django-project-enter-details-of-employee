# Generated by Django 2.1.2 on 2018-11-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genericviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='company_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='mobile',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]