# Generated by Django 4.1.9 on 2023-07-06 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gptApp', '0013_category_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
