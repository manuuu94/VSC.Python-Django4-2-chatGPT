# Generated by Django 4.1.9 on 2023-07-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gptApp', '0019_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]