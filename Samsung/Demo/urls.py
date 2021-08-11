from django.contrib import admin
from django.urls import path, include

from .views import MyForm, display, home, menu, newdevices,  Notify

urlpatterns = [
path('',home, name='home'),
path('menu/',menu, name='menu'),
path('details/',MyForm.as_view(), name='homepage'),
path('display/', display, name='display'),
path('newdevices/',newdevices,name='newdevices'),
path('email/',Notify.as_view(),name='email'),
]