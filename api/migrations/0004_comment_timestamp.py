# Generated by Django 3.2.6 on 2021-08-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210814_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timeStamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
