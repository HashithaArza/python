from django.db import models
CHOICE = (
        ('yes', 'YES'),
        ('no', 'NO'),
    )
# Create your models here.
class SpecForm(models.Model):
    name=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    price=models.IntegerField()
    release_date=models.DateField()
    form_factor=models.CharField(max_length=50)
    dimentions1=models.IntegerField()
    dimentions2=models.IntegerField()
    dimentions3=models.IntegerField()
    weight=models.CharField(max_length=50)
    battery_capacity=models.CharField(max_length=50)
    removable_battery=models.CharField(max_length=6, choices=CHOICE, default='no')
    color=models.CharField(max_length=50)
    #connectivity
    wifi=models.CharField(max_length=6, choices=CHOICE, default='yes')
    wifi_standards=models.CharField(max_length=50)
    gps=models.CharField(max_length=6, choices=CHOICE, default='yes')
    bluetooth=models.CharField(max_length=6, choices=CHOICE, default='yes')
    bluetooth_version=models.CharField(max_length=50)
    memory_card=models.CharField(max_length=6, choices=CHOICE, default='yes')
    memory_card_storage=models.IntegerField()
    gpu=models.CharField(max_length=6, choices=CHOICE, default='yes')
    gpu_value=models.CharField(max_length=50)

    nfc=models.CharField(max_length=6, choices=CHOICE, default='yes')
    infrared=models.CharField(max_length=6, choices=CHOICE, default='yes')
    usb_otg=models.CharField(max_length=6, choices=CHOICE, default='yes')
    fm=models.CharField(max_length=6, choices=CHOICE, default='yes')
    wifi_direct=models.CharField(max_length=6, choices=CHOICE, default='yes')
    number_of_sims=models.IntegerField()
    mhl=models.CharField(max_length=6, choices=CHOICE, default='yes')
    gsma_cdma=models.CharField(max_length=50)
    sim_type=models.CharField(max_length=50)
    three_g=models.CharField(max_length=6, choices=CHOICE, default='yes')
    four_g=models.CharField(max_length=6, choices=CHOICE, default='yes')
    support_4g=models.CharField(max_length=6, choices=CHOICE, default='yes')
    #display
    screen_size=models.CharField(max_length=50)
    touch_screen=models.CharField(max_length=6, choices=CHOICE, default='yes')
    resolution1=models.CharField(max_length=50)
    resolution2=models.CharField(max_length=50)
    #Hardware
    processor=models.CharField(max_length=50)
    processor_make=models.CharField(max_length=50)
    ram=models.IntegerField()
    internal_storage=models.IntegerField()
    expandable_storage=models.IntegerField()

    #software
    os=models.CharField(max_length=50)
    browser_version=models.CharField(max_length=50)

    #camera
    camera_type=models.CharField(max_length=50)
    rear_camera=models.CharField(max_length=50)
    front_camera=models.CharField(max_length=50)
    rear_flash=models.CharField(max_length=6, choices=CHOICE, default='yes')

    #Sensors
    fingerprint_scanner=models.CharField(max_length=6, choices=CHOICE, default='yes')
    face_recognition=models.CharField(max_length=6, choices=CHOICE, default='yes')
    compass_magnetometer=models.CharField(max_length=6, choices=CHOICE, default='yes')
    accelerometer=models.CharField(max_length=6, choices=CHOICE, default='yes')
    light_sensor=models.CharField(max_length=6, choices=CHOICE, default='yes')
    gryoscope=models.CharField(max_length=6, choices=CHOICE, default='yes')
    barometer=models.CharField(max_length=6, choices=CHOICE, default='yes')
    temperature_sensor=models.CharField(max_length=6, choices=CHOICE, default='yes')

    class Meta:
        db_table = 'spec_form'

class Notification(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)

    class Meta:
        db_table = 'notification'
