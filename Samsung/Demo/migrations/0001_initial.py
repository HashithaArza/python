# Generated by Django 3.1.7 on 2021-06-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('rdate', models.DateTimeField()),
                ('weight', models.CharField(max_length=30)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('rearcamera', models.IntegerField()),
                ('frontcamera', models.IntegerField()),
                ('os', models.CharField(max_length=50)),
                ('battery', models.IntegerField()),
            ],
            options={
                'db_table': 'mobiles_spec',
            },
        ),
        migrations.CreateModel(
            name='SpecForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('release_date', models.DateField()),
                ('form_factor', models.CharField(max_length=50)),
                ('dimentions1', models.IntegerField()),
                ('dimentions2', models.IntegerField()),
                ('dimentions3', models.IntegerField()),
                ('weight', models.CharField(max_length=50)),
                ('battery_capacity', models.CharField(max_length=50)),
                ('removable_battery', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='no', max_length=6)),
                ('color', models.CharField(max_length=50)),
                ('wifi', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('wifi_standards', models.CharField(max_length=50)),
                ('gps', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('bluetooth', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('bluetooth_version', models.CharField(max_length=50)),
                ('memory_card', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('memory_card_storage', models.IntegerField()),
                ('gpu', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('gpu_value', models.CharField(max_length=50)),
                ('fyi', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('nfc', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('infrared', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('usb_otg', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('fm', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('wifi_direct', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('number_of_sims', models.IntegerField()),
                ('mhl', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('gsma_cdma', models.CharField(max_length=50)),
                ('sim_type', models.CharField(max_length=50)),
                ('three_g', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('four_g', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('support_4g', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('screen_size', models.CharField(max_length=50)),
                ('touch_screen', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('resolution1', models.CharField(max_length=50)),
                ('resolution2', models.CharField(max_length=50)),
                ('processor', models.CharField(max_length=50)),
                ('processor_make', models.CharField(max_length=50)),
                ('ram', models.IntegerField()),
                ('internal_storage', models.IntegerField()),
                ('expandable_storage', models.IntegerField()),
                ('os', models.CharField(max_length=50)),
                ('browser_version', models.CharField(max_length=50)),
                ('camera_type', models.CharField(max_length=50)),
                ('rear_camera', models.CharField(max_length=50)),
                ('front_camera', models.CharField(max_length=50)),
                ('rear_flash', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('fingerprint_scanner', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('face_recognition', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('compass_magnetometer', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('accelerometer', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('light_sensor', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('gryoscope', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('barometer', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
                ('temperature_sensor', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=6)),
            ],
            options={
                'db_table': 'spec_form',
            },
        ),
    ]
