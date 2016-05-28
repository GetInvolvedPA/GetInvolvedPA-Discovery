from django.contrib import admin

from .models import Student, Service_Classification, Service, Service_Activiy

admin.site.register(Student)
admin.site.register(Service_Classification)
admin.site.register(Service)
admin.site.register(Service_Activiy)