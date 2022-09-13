from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import blogs,register_doctor
from .forms import *
from datetime import timedelta, datetime

# Create your views here.



usernames=[]
def home(request):
    return render(request,'home.html')


def registers(request):
    if request.method=='POST':

        #checking the entered username is avalilable or not
        user_name = request.POST.get('user_name')
        existed_user=register_doctor.objects.filter(user_name=user_name).first()

        #if entered username is not available
        if existed_user is not None:
            messages.warning(request,user_name+' user name is not available ! please try another ')
            return render(request,'register.html')

        #checking the password and confirm password are same
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        if password !=password2:
            messages.warning(request,'passwords are not matching')
            return render(request,'register.html')


        form=doctors(request.POST,request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid():
                form.save()
                messages.success(request,'registered successfully')
                return render(request, 'signin.html')
        else:
                messages.warning(request,'error occur')


    return render(request,'register.html')

def signin(request):
    if request.method=='POST':
        #cheking the user have account or not
        username = request.POST.get('user_name')
        if len(usernames)!=0:
            for i in range(len(usernames)):
                del usernames[i]

        usernames.append(username)
        password=request.POST.get('password')
        auth=register_doctor.objects.filter(user_name=username,password=password).first()

        #authenticating the user

        if auth is not None:
            message=username+' logged in successfully'
            messages.success(request,message)
            return render(request,'dashboard.html',{'context':auth})
        else:
            message = username + ' enter details correctly !'
            messages.warning(request,message)
            return render(request,'signin.html')

    return render(request,'signin.html')
blogno=-1
def createblog(request):
    print(usernames)

    if request.method=='POST':
        user = request.POST.get('user_name')
        print('user')
        usernames.append(user)
        print(usernames)
        form=blogsform(request.POST,request.FILES)

        if form.is_valid():
            messages.success(request,'successfully uploaded')
            form.save()
        else:
            messages.warning(request,'error occured while uploading please try again !')
        global blogno

        if blogno is not None:
            blogs.objects.filter(id=blogno).delete()
        print('username',usernames)
    return render(request,'createblogs.html',{'context':usernames[0]})

def showblog(request):
    print(usernames)
    users = register_doctor.objects.filter(user_name=usernames[0]).first()
    #blog=blogs.objects.filter(user_name=usernames[0],draft=False)
    print(users)
    user_type=users.user_type
    print(user_type)
    if user_type=='patient':
        blog=blogs.objects.filter(draft='False')
        if len(blog)==0:
            return HttpResponse('there are no blogs present right now !')
        print(blog)
    else:
        blog = blogs.objects.filter(user_name=usernames[0],draft='False')
    print(len(blog))
    if len(blog) ==0 :
        return HttpResponse('there are no blogs made by you!')
    else:
        print(user_type)

        return render(request,'viewblog.html',{'context':blog,'username':usernames[0],'user_type':user_type})


def showdraft(request):
    print(usernames)
    blog=blogs.objects.filter(user_name=usernames[0],draft='True').first()
    if blog is not None:
        global blogno
        blogno=blog.id
    else:
        return HttpResponse(usernames[0]+'! there are no drafts saved buy you !')
    #print(blogno)
    return render(request,'createblogs.html',{'blog':blog,'context':usernames[0],'user_type':'doctor','draft':'True'})



def showappointments(request,user_name):
    name=user_name
    user=register_doctor.objects.filter(user_name=name).first()
    user_type=user.user_type
    if user_type == 'doctor':
        appointment=appointments.objects.filter(doctor_name=name)
    else:
        appointment=appointments.objects.filter(patient_name=name)

    if len(appointment)== 0:
        return HttpResponse(name+' no appointments are present there for you !')
    else:
        return render(request,'appointments.html',{'appointment':appointment,'user_type':user_type})

def bookappointments(request,patient_name):
    name=patient_name
    doctors=register_doctor.objects.filter(user_type='doctor')
    return render(request,'showdoctors.html',{'doctors':doctors,'patient_name':name})
    #return HttpResponse(name+' no appointments are present there for you !')

def appointment(request,patient_name,doctor_name):
    print(patient_name+'-'+doctor_name)
    return render(request,'appointmentform.html',{'patient_name':patient_name,'doctor_name':doctor_name})
    #return HttpResponse(patient_name+' '+doctor_name+' '+' no appointments are present there for you !')

def bookanappointment(request):
    required_speciality=request.POST.get('required_speciality')
    date=request.POST.get('appointment_date')
    time=request.POST.get('appointment_time')
    print(date,time)
    patient_name=request.POST.get('patient_name')
    doctor_name=request.POST.get('doctor_name')
    if patient_name is None and doctor_name is None:
        messages.warning(request,'session timed out sign in again')
        return render(request,'appointmentform.html')

    time = datetime.strptime(time, '%H:%M')
    d = datetime.now().date()
    endtime = datetime(d.year, d.month, d.day, time.hour, time.minute, time.second,
                       time.microsecond) + timedelta(minutes=45)

    appointment=appointments.objects.filter(doctor_name=doctor_name,appointment_date=date)
    # calculating appoint ment starting time before 45 minutes
    print(appointment)
    time = datetime(d.year, d.month, d.day, time.hour, time.minute, time.second)
    print(type(time))

    # calulating the session 45 minutes
    for i in appointment:
        print(type(i.appointment_starttime))
        print(type(i.appointment_endtime))
        i.appointment_starttime=datetime(d.year, d.month, d.day,i.appointment_starttime.hour,i.appointment_starttime.minute,i.appointment_starttime.second)
        i.appointment_endtime=datetime(d.year, d.month, d.day,i.appointment_endtime.hour,i.appointment_endtime.minute,i.appointment_endtime.second)
        appointmentstarttime=datetime(d.year, d.month, d.day,i.appointment_starttime.hour,i.appointment_starttime.minute,i.appointment_starttime.second)-timedelta(minutes=45)
        print(appointmentstarttime,type(appointmentstarttime))
        print(i.appointment_starttime,time,i.appointment_endtime)
        if i.appointment_starttime <= time <= i.appointment_endtime:
            messages.warning(request,'time slot is already booked')
            return render(request,'appointmentform.html',{'patient_name':patient_name,'doctor_name':doctor_name})


    from .calsetup import get_calendar_service
    import sys
    sys.path.insert(1,'D:\\files\\python\\pythonpractice\\numpy\\')
    import createevent


    createevent.main(str(time))




    bookappointment = appointments.objects.create(patient_name=patient_name, doctor_name=doctor_name,
                                                  required_speciality=required_speciality, appointment_date=date,
                                                  appointment_starttime=time,appointment_endtime=endtime)
    bookappointment.save()

    #messages.success(request,'time slot is booked for you !')
    bookappointment.appointment_starttime=bookappointment.appointment_starttime.strftime("%H:%M:%S")
    print(bookappointment.appointment_starttime)
    bookappointment.appointment_endtime = bookappointment.appointment_endtime.strftime("%H:%M:%S")
    print(bookappointment.appointment_endtime)

    return render(request, 'showappointment.html',{'patient_name':patient_name,'doctor_name':doctor_name,'context':bookappointment})




'''        '{:%H:%M}'.format(i.appointment_time)
        print(i.appointment_time)
        # calculating endtime for appointment time
        endtime=datetime(1970, 1, 1, i.appointment_time.hour, i.appointment_time.minute, i.appointment_time.second,
                    i.appointment_time.microsecond) + timedelta(minutes=45)
        starttime=datetime(1970, 1, 1,i.appointment_time.hour, i.appointment_time.minute, i.appointment_time.second)

        time = datetime.strptime(time, '%H:%M')
        appointmentstartingtime = datetime(1970, 1, 1, i.appointment_time.hour, i.appointment_time.minute,
                                           i.appointment_time.second,
                                           i.appointment_time.microsecond) - timedelta(minutes=45)
    
    

       time=datetime(1970, 1, 1,time.hour,time.minute,time.second)
        print(endtime)
        print(starttime)
        print(time)
        print(appointmentstartingtime)
        if appointmentstartingtime<time:
            print(True,time,appointmentstartingtime)
        else:
            print(False,time,appointmentstartingtime)
        # time formatting
        '{:%H:%M}'.format(time)
        print(time)
        #print(type(i.appointment_time))
        if starttime<time<endtime and time>appointmentstartingtime:
            return HttpResponse("not possible to book an appointment")

    else:
        bookappointment = appointments.objects.create(patient_name=patient_name, doctor_name=doctor_name,
                                                      required_speciality=required_speciality, appointment_date=date,
                                                      appointment_time=time)
        bookappointment.save()
        return HttpResponse('appointment booked')
    for i in appointment:
        print(appointment)'''


