# Generated by Django 2.2.1 on 2019-05-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0004_auto_20190520_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='comments_number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
