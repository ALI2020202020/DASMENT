# Generated by Django 3.1.2 on 2020-10-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0003_auto_20201028_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='LA', max_length=30),
        ),
    ]
