# Generated by Django 4.1.4 on 2022-12-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fuel_UR_Way', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='car',
            old_name='owner',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='car',
            name='carType',
        ),
        migrations.RemoveField(
            model_name='car',
            name='fuleType',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('litter', models.IntegerField()),
                ('address', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.FloatField()),
                ('car', models.ManyToManyField(related_name='userCar', to='Fuel_UR_Way.car')),
                ('payed', models.ManyToManyField(related_name='methods', to='Fuel_UR_Way.payments')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='carType',
            field=models.ManyToManyField(related_name='type', to='Fuel_UR_Way.cartype'),
        ),
        migrations.AddField(
            model_name='car',
            name='fuleType',
            field=models.ManyToManyField(related_name='type', to='Fuel_UR_Way.fueltype'),
        ),
    ]
