# Generated by Django 5.0.6 on 2024-07-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0009_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default='0'),
        ),
    ]
