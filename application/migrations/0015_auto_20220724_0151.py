# Generated by Django 3.2.8 on 2022-07-24 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_auto_20220724_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='et0',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='et0',
            name='Time_Stamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
