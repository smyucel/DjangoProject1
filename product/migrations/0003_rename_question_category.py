# Generated by Django 5.1.7 on 2025-04-18 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_question_keywords_alter_question_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Category',
        ),
    ]
