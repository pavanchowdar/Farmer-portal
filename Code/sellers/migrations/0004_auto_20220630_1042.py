# Generated by Django 2.2 on 2022-06-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0003_auto_20220630_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerscropdatamodels',
            name='cdate',
            field=models.DateField(auto_now=True),
        ),
    ]
