# Generated by Django 4.1.9 on 2023-06-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_cv', '0008_alter_workxp_todate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workxp',
            name='toDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
