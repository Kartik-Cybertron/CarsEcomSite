# Generated by Django 3.1.2 on 2021-02-25 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('transmission', models.CharField(max_length=200)),
                ('fueltype', models.CharField(max_length=200)),
                ('seating_capacity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bentley',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('transmission', models.CharField(max_length=200)),
                ('fueltype', models.CharField(max_length=200)),
                ('seating_capacity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BMW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('transmission', models.CharField(max_length=200)),
                ('fueltype', models.CharField(max_length=200)),
                ('seating_capacity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Jaguar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('transmission', models.CharField(max_length=200)),
                ('fueltype', models.CharField(max_length=200)),
                ('seating_capacity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lambo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('transmission', models.CharField(max_length=200)),
                ('fueltype', models.CharField(max_length=200)),
                ('seating_capacity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200)),
                ('l_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('images', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mercedes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('transmission', models.CharField(max_length=200)),
                ('fueltype', models.CharField(max_length=200)),
                ('seating_capacity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('transmission', models.CharField(max_length=200)),
                ('fueltype', models.CharField(max_length=200)),
                ('seating_capacity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('log', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CarsApp.log')),
            ],
        ),
    ]
