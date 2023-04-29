from django.db import models
from django.utils import timezone

class Organizer(models.Model):
    Summercamp_Id=models.CharField(max_length=20,primary_key=True)
    Password=models.CharField(max_length=45,null=False)
    CampName=models.CharField(max_length=50,null=False)
    OwnerName=models.CharField(max_length=40,null=False)
    CampEmailid=models.EmailField(max_length=45,null=False)
    CampMobileno=models.CharField(max_length=10,null=False)
    CampAddress=models.CharField(max_length=100,null=False)
    Description=models.TextField(null=False)
    def __str__(self):
        return self.CampName

class Feedback(models.Model):
    Feedback_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=45,null=False)
    Email=models.EmailField(max_length=45,null=False)
    CampName=models.CharField(max_length=100,null=False)
    Date=models.DateField(default=timezone.now)
    FeedbackText=models.TextField(null=False)
    Rating=models.IntegerField(null=False)
    def __str__(self):
        return self.Name

class Program_detail(models.Model):
    Summercamp_Id=models.CharField(max_length=30)
    Program_Id=models.AutoField(primary_key=True)
    ProgramName=models.CharField(max_length=100,null=False)
    Duration=models.CharField(max_length=20,null=False)
    Fees=models.CharField(max_length=30,null=False)
    StartDate=models.DateField(default=timezone.now)
    EndDate=models.DateField(default=timezone.now)
    Description=models.TextField(default=timezone.now)
    AgeGroup=models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.ProgramName

class Job_Description(models.Model):
    Summercamp_Id=models.CharField(max_length=30)
    Job_Id=models.CharField(max_length=30,primary_key=True)
    PostName=models.CharField(max_length=30,null=False)
    No_ofseats=models.IntegerField(null=False)
    LastDatetoapply=models.DateField(null=False)
    Postdate=models.DateField(default=timezone.now)
    Description=models.TextField(null=False)
    def __str__(self):
        return self.PostName

class CityEvent(models.Model):
    Event_Id=models.AutoField(primary_key=True)  
    Eventname=models.CharField(max_length=100,null=False)      
    Date=models.DateField(default=timezone.now)
    City=models.CharField(max_length=50,null=False)
    VenueAddress=models.TextField(null=False)
    Description=models.TextField()
    EventPic=models.ImageField(max_length=255,upload_to="summercamp/event_pic",default="")
    def __str__(self):
        return self.Eventname
    


class Contact(models.Model):
    Name=models.CharField(max_length=45,primary_key=True)
    Email=models.EmailField(max_length=45,null=False)
    Phone=models.CharField(max_length=10,null=False)
    Question=models.TextField(null=False)
    Date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.Name

# Create your models here.
