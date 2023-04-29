from django.contrib import admin

from . models import Organizer,Feedback,Program_detail,Job_Description,CityEvent,Contact

admin.site.register(Organizer)
admin.site.register(Feedback)
admin.site.register(Program_detail)
admin.site.register(Job_Description)
admin.site.register(CityEvent)
admin.site.register(Contact)
# Register your models here.
