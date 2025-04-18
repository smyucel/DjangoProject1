# Generated by Django 5.1.7 on 2025-04-17 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='keywords',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
