from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from .views import *


urlpatterns = [
    path('upload/createblogs',createblog,name='createblogs'),
    path('upload/showdraft',showdraft,name='showdraft'),
    path('viewblogs',showblog,name='viewblogs'),
    path('upload/registers',registers,name='registers'),
    path('upload/',signin,name='signin'),
    path('upload/signin/signin',signin,name='signin/signin'),
    path('upload/showappointment/<str:user_name>/',showappointments,name='showappointment'),
    path('upload/bookappointment/<str:patient_name>/', bookappointments, name='bookappointment'),
    path('upload/appointment/<str:patient_name>,<str:doctor_name>/',appointment,name='appointment'),
    path('upload/bookanappointment',bookanappointment,name='bookanappointment'),
]

