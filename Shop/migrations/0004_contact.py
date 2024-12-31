# Generated by Django 5.0.6 on 2024-07-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=65)),
                ('phone', models.CharField(default='', max_length=15)),
                ('desc', models.CharField(default='', max_length=5000)),
            ],
        ),
    ]