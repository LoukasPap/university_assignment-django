# Generated by Django 3.0.3 on 2020-02-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebarber', '0005_auto_20200226_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barbershop',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
