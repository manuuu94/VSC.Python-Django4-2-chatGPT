# Generated by Django 4.1.9 on 2023-07-03 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_cv', '0015_education_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='otherValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='my_cv/static/my_cv/img/profile')),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='progress',
            field=models.IntegerField(),
        ),
    ]
