import datetime
import email
from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('doctor', 'doctor'),
    ('patient', 'patient'),
)
class register_doctor(models.Model):
    #model for entered details
    user_type=models.CharField(choices=GENDER_CHOICES,max_length=10,default='doctor')
    first_name=models.CharField(max_length=25,null=True,blank=True)
    last_name = models.CharField(max_length=25,null=True)
    user_name = models.CharField(max_length=25,null=True)
    profile_pic = models.ImageField(upload_to='images/',null=True)
    address_line1=models.CharField(max_length=75,null=True)
    city=models.CharField(max_length=25,null=True,blank=True)
    state=models.CharField(max_length=25,null=True)
    pincode=models.IntegerField(null=True)
    email=models.EmailField(max_length=25,null=True)
    password=models.CharField(max_length=25,null=True)
    password2=models.CharField(max_length=25,null=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'register_doctor'

category_CHOICES = (
    ('Mental health','Mental health'),
    ('covid 19','covid 19'),
    ('heart disease','heart disease'),
    ('immunization','immunization')
)
drafts=(
    ('True','True'),
    ('False','False')
)
class blogs(models.Model):
    user_name = models.CharField(max_length=25, null=True)
    title=models.CharField(max_length=25, null=True)
    image=models.FileField(upload_to='blogimages/',null=True)
    category=models.CharField(choices=category_CHOICES,max_length=25)
    summary=models.CharField(max_length=1500,null=True)
    content=models.CharField(max_length=10000,null=True)
    draft=models.CharField(choices=drafts,max_length=5,null=True,default='False')
    def summary_as_list(self):
        return self.summary.split(" ")

    def __str__(self):
        return self.user_name

class appointments(models.Model):
    patient_name=models.CharField(max_length=25,null=True)
    doctor_name=models.CharField(max_length=25,null=True)
    required_speciality=models.CharField(max_length=25,null=True)
    appointment_date=models.DateField(default=datetime.date)
    appointment_starttime=models.TimeField(default=datetime.datetime.now)
    appointment_endtime=models.TimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.patient_name+' '+self.doctor_name







