# Generated by Django 2.2.1 on 2019-05-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0010_auto_20190522_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='communication',
            field=models.DecimalField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], decimal_places=0, default=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='marking',
            field=models.DecimalField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], decimal_places=0, default=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='objectivity',
            field=models.DecimalField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], decimal_places=0, default=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='quality',
            field=models.DecimalField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], decimal_places=0, default=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=400),
        ),
    ]
