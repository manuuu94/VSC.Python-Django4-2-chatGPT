# Generated by Django 4.1.9 on 2023-07-09 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gptApp', '0017_alter_question_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
