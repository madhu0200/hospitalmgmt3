from django import forms
from .models import *

class doctors(forms.ModelForm):
    class Meta:
        model=register_doctor

        fields=['user_type','first_name','last_name','user_name','profile_pic','address_line1','city','state','pincode','email','password','password2']

class blogsform(forms.ModelForm):
    class Meta:
        model=blogs
        fields=['user_name','title','category','summary','image','content','draft']

class appointmentForm(forms.ModelForm):
    class Meta:
        model=appointments
        fields=['patient_name','doctor_name','required_speciality','appointment_date','appointment_starttime','appointment_endtime']
