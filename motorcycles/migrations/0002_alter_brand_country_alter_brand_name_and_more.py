# Generated by Django 5.1.2 on 2024-10-21 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='engine',
            name='capacity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='engine',
            name='fuel_type',
            field=models.CharField(choices=[('Petrol', 'Petrol'), ('Electric', 'Electric')], max_length=50),
        ),
        migrations.AlterField(
            model_name='engine',
            name='power',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='motorcycles.category'),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='model',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='year_of_manufacture',
            field=models.PositiveIntegerField(),
        ),
    ]