from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from django.views import View
from .models import SpecForm,Notification
import mysql.connector;

class MyForm(View):
    def get(self, request):
        return render(request, 'mobilespecs.html')
    def post(self, request):
        if request.method=='POST':
            form=SpecForm()
            form.name= request.POST.get("name")
            form.model =request.POST.get("model")
            form.price =request.POST.get("price")
            form.release_date =request.POST.get("release_date")
            form.form_factor =request.POST.get("form_factor")
            form.dimentions1 =request.POST.get("dimentions1")
            form.dimentions2 =request.POST.get("dimentions2")
            form.dimentions3 =request.POST.get("dimentions3")
            form.weight =request.POST.get("weight")
            form.battery_capacity =request.POST.get("battery_capacity")
            form.removable_battery =request.POST.get("removable_battery")
            form.color = request.POST.get("colour")
            form.wifi = request.POST.get("wifi")
            form.wifi_standards = request.POST.get("wifi_standards")
            form.gps = request.POST.get("gps")
            form.bluetooth = request.POST.get("bluetooth")
            form.bluetooth_version = request.POST.get("bluetooth_version")
            form.memory_card = request.POST.get("memorycard")
            form.memory_card_storage = request.POST.get("memorycard_storage")
            form.gpu = request.POST.get("gpu")
            form.gpu_value = request.POST.get("gpu_model")

            form.nfc = request.POST.get("nfc")
            form.infrared = request.POST.get("infrared")
            form.usb_otg = request.POST.get("usb_otg")
            form.fm = request.POST.get("fm")
            form.wifi_direct = request.POST.get("wifi_direct")
            form.number_of_sims = request.POST.get("no_of_sims")
            form.mhl = request.POST.get("mhl")
            form.gsma_cdma = request.POST.get("gsma_cdma")
            form.sim_type = request.POST.get("sim_type")
            form.three_g = request.POST.get("3g")
            form.four_g = request.POST.get("4g")
            form.support_4g = request.POST.get("4g_support")
            form.screen_size = request.POST.get("screen_size")
            form.touch_screen = request.POST.get("touch_screen")
            form.resolution1 = request.POST.get("resolution1")
            form.resolution2 = request.POST.get("resolution2")
            form.processor = request.POST.get("processor")
            form.processor_make = request.POST.get("processor_make")
            form.ram = request.POST.get("ram")
            form.internal_storage = request.POST.get("internal_storage")
            form.expandable_storage = request.POST.get("expandable_memory")
            form.os = request.POST.get("operating_system")
            form.browser_version = request.POST.get("browser_version")
            form.camera_type = request.POST.get("camera_type")
            form.rear_camera = request.POST.get("rear_camera")
            form.front_camera = request.POST.get("front_camera")
            form.rear_flash = request.POST.get("rear_flash")
            form.fingerprint_scanner = request.POST.get("fingerprint_scanner")
            form.face_recognition = request.POST.get("face_recognition")
            form.compass_magnetometer = request.POST.get("compass")
            form.accelerometer = request.POST.get("accelerometer")
            form.light_sensor = request.POST.get("ambient_light_sensor")
            form.gryoscope = request.POST.get("gyroscope")
            form.barometer = request.POST.get("barometer")
            form.temperature_sensor = request.POST.get("temperature_sensor")
            form.save()
            print("Record saved")


def display(request):
    if request.method=='GET':
        mobiles = SpecForm.objects.all()
        return render(request, 'display.html', {'mobiles':mobiles})
def home(request):
    return render(request, 'home.html')
def menu(request):
    return render(request, 'menu.html')
def newdevices(request):
    if request.method=='GET':
        mydb = mysql.connector.connect(host="localhost", user="root", password="H@shith@13", database="samsung");
        cur = mydb.cursor();
        cur.execute("select ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS SNO,name,date,chipset,battery,storage,ram from SamsungDetails")
        result=cur.fetchall();
        i=0
        return render(request, 'newlyLaunchedDevices.html', {'result': result,'i':i})

class Notify(View):
    def get(self,request):
        return render(request, 'email.html')


    def post(self,request):
        if request.method=='POST':
            form=Notification()
            form.name= request.POST.get("name")
            form.email = request.POST.get("email")
            form.save()
            notifications = Notification.objects.all()
            mydb = mysql.connector.connect(host="localhost", user="root", password="H@shith@13", database="samsung");
            cur = mydb.cursor();
            cur.execute(
                "select ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS SNO,name,date,chipset,battery,storage,ram from SamsungDetails")
            result = cur.fetchall();
            str1=''
            i=0
            for obj in result:
                str1+=str(obj)
                str1+="\n"
                i=i+1
                if i==26:
                    break
            #str1=str1.split('\n')
            send_mail('Hello this is SAMSUNG',
                      str1,
                  'samsungprismse22klu@gmail.com',
                  [obj.email for obj in notifications],
                  fail_silently=False)
            return HttpResponse("<h1>THE EMAIL HAS BEEN SENT!!</h1>")







