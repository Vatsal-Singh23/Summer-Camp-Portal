from django.forms import PasswordInput
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.http import JsonResponse
from django.contrib import messages



from .models import Feedback
from .models import Contact
from .models import Organizer
from .models import Job_Description
from .models import Program_detail
from .models import CityEvent


def home(request):
    cityevents_set=CityEvent.objects.all()
    feedback_set=Feedback.objects.all()
    context={

        "cityeventsinfo":cityevents_set,
        "feedbackinfo":feedback_set

    }
    return render(request,'summercamp/home.html',context)

def aboutus(request):
    return render(request,'summercamp/aboutus.html')    

def feedback(request):
    return render(request,'summercamp/feedback.html')

def query(request):
    if request.method=="POST":
        cname=request.POST["txtname"]
        cemail=request.POST["txtemail"]
        cphone=request.POST["txtphonenumber"]
        cquery=request.POST["txtquery"]
        cdate=request.POST["txtdate"]
        print(cname,cemail,cphone,cquery,cdate)
        contactus_obj=Contact(Name=cname,Email=cemail,Phone=cphone,Question=cquery,Date=cdate)#ORM
        contactus_obj.save()#ORM
        messages.success(request,"Thanks for Contacting Us")

    return render(request,'summercamp/query.html')

def feedback(request):
    if request.method=="POST":
        fname=request.POST["txtname"]
        femail=request.POST["txtemail"]
        fcamp_name=request.POST["txtcampname"]
        ftext=request.POST["txtaddress"]
        fdate=request.POST["txtdate"]
        frating=request.POST["rating"]
        feedback_obj=Feedback(Name=fname,Email=femail,CampName=fcamp_name,FeedbackText=ftext,Date=fdate,Rating=frating)
        feedback_obj.save()
        messages.success(request,"Thank You")
        

    return render(request,'summercamp/feedback.html')    

 #Create your views here.

def registration(request):
    if request.method=="POST":
        rcamp_id=request.POST["txtid"]
        rpassword=request.POST["txtpassword"]
        rcamp_name=request.POST["txtcampname"]
        rowner_name=request.POST["txtownername"]
        rcamp_email=request.POST["txtcampemail"]
        rcamp_phone=request.POST["txtnumber"]
        rcamp_address=request.POST["txtaddress"]
        rdescription=request.POST["txtdescription"]
        organizer_obj=Organizer(Summercamp_Id=rcamp_id,Password=rpassword,CampName=rcamp_name,OwnerName=rowner_name,CampEmailid=rcamp_email,CampMobileno=rcamp_phone,CampAddress=rcamp_address,Description=rdescription)
        organizer_obj.save()
        messages.success(request,"Registration Done Successfully")

    return render(request,'summercamp/registration.html')


def login(request):
    if request.method=="GET":
        return render(request,'summercamp/login.html')

    if request.method=="POST":    
        campid=request.POST["txtid"]
        camppassword=request.POST["txtpassword"]
        # print(campid,camppassword)
        organizer_obj=Organizer.objects.filter(Summercamp_Id=campid,Password=camppassword)
        if len(organizer_obj)>0:
            request.session["session_id"]=campid
            context={
                "organizer_data":organizer_obj
            }
            return render(request,'summercamp/organizer/organizer_home.html',context)
        
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("login")

def organizer_home(request):
     campid=request.session["session_id"]
     organizer_obj=Organizer.objects.filter(Summercamp_Id=campid)
     context={
                "organizer_data":organizer_obj
     }

     return render(request,'summercamp/organizer/organizer_home.html',context)   


def add_job(request):
    if request.method=="POST":

        campid=request.session["session_id"]
        # organizer_obj=Organizer.objects.get(Summercamp_Id=campid)
        print(campid)
        rjob_id=request.POST["txtjobid"]
        rpostname=request.POST["txtpostname"]
        rno_ofseats=request.POST["txtseats"]
        rlastdate=request.POST["txtldate"]
        rpostdate=request.POST["txtdate"]
        rjobdescription=request.POST["txtjobdescription"]
        jobdetails_obj=Job_Description(Summercamp_Id=campid,Job_Id=rjob_id,PostName=rpostname,No_ofseats=rno_ofseats,LastDatetoapply=rlastdate,Postdate=rpostdate,Description=rjobdescription)
        jobdetails_obj.save()
        messages.success(request,"Job Details Added  Successfully")

    return render(request,'summercamp/organizer/job_description.html')   

def logout(request):
    del request.session["session_id"]
    return render(request,'summercamp/login.html')

def add(request):

    if request.method=="POST":

        campid=request.session["session_id"]
        # organizer_obj=Organizer.objects.get(Summercamp_Id=campid)
        print(campid)
        rprogramname=request.POST["txtprogramname"]
        rduration=request.POST["txtduration"]
        rfees=request.POST["txtfees"]
        rstartdate=request.POST["txtsdate"]
        renddate=request.POST["txtedate"]
        rprogramdescription=request.POST["txtprogramdescription"]
        ragegroup=request.POST["txtage"]
        programdetails_obj=Program_detail(Summercamp_Id=campid,ProgramName=rprogramname,Duration=rduration,Fees=rfees,StartDate=rstartdate,EndDate=renddate,Description=rprogramdescription,AgeGroup=ragegroup)
        programdetails_obj.save()
        messages.success(request,"Program Details Added  Successfully")

    return render(request,"summercamp/organizer/program_details.html")  



def edit_profile(request):
    campid=request.session["session_id"]
    print(campid)
    organizer_obj=Organizer.objects.get(Summercamp_Id=campid)
    print(organizer_obj.CampName)
    context={
        "organizer_data":organizer_obj
    }
    if request.method=="POST":
        campname=request.POST["txtcampname"]
        ownername=request.POST["txtownername"]
        campemailid=request.POST["txtcampemail"]
        campnumber=request.POST["txtnumber"]
        campaddress=request.POST["txtaddress"]
        description=request.POST["txtdescription"]
        print(campname,campnumber,campaddress)
        organizer_obj=Organizer.objects.filter(Summercamp_Id=campid)
        organizer_obj.update(CampName=campname,OwnerName=ownername,CampEmailid=campemailid,CampMobileno=campnumber,CampAddress=campaddress,Description=description)
        return redirect("organizer_home")
        
    return render(request,"summercamp/organizer/edit_profile.html",context)  

def events(request):
    event_set=CityEvent.objects.all()
    context={"eventinfo":event_set}
    return render(request,"summercamp/events.html",context)

def program(request):
    program_set=Program_detail.objects.all()
    context={"programinfo":program_set}
    return render(request,"summercamp/program.html",context)    

def employment(request):
    job_set=Job_Description.objects.all()
    context={"jobinfo":job_set}
    return render(request,"summercamp/employment.html",context)

def update(request):
    campid=request.session["session_id"]
    print(campid)
    program_set=Program_detail.objects.get(Summercamp_Id=campid)
    context={
        "programinfo":program_set
    }
    if request.method=="POST":
        programname=request.POST["txtprogramname"]
        duration=request.POST["txtduration"]
        fees=request.POST["txtfees"]
        startdate=request.POST["txtsdate"]
        enddate=request.POST["txtedate"]
        programdescription=request.POST["txtprogramdescription"]
        agegroup=request.POST["txtage"]
        program_set=Program_detail.objects.filter(Summercamp_Id=campid)
        program_set.update(ProgramName=programname,Duration=duration,Fees=fees,StartDate=startdate,EndDate=enddate,Description=programdescription,AgeGroup=agegroup)
        return redirect("organizer_home")

    return render(request,"summercamp/organizer/editprogram_details.html",context)