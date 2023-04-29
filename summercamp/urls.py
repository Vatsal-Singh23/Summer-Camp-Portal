from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.aboutus,name="about"),
    path('query',views.query,name="query"),
    path('feedback',views.feedback,name="feedback"),
    path('login',views.login,name="login"),
    path('registration',views.registration,name="registration"),
    path('add_job',views.add_job,name="add_job"),
    path('organizer_home',views.organizer_home,name="organizer_home"),
    path('logout',views.logout,name="logout"),
    path('add',views.add,name="add"),
    path('update',views.update,name="update"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('events',views.events,name="events"),
    path('employment',views.employment,name="employment"),
    path('program',views.program,name="program")
]