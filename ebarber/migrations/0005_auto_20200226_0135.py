# Generated by Django 3.0.3 on 2020-02-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebarber', '0004_auto_20200225_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barbershop',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
