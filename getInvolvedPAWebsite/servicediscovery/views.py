#!/usr/bin/python
#
# Views.py
# get involvedPA

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone
from servicediscovery.models import Student, Service_Classification, Service, Service_Activiy

def get_data_for_service_class(all_objects):
    data = []
    for classification in all_objects:
        data.append((classification.class_name, classification.id))
    return data

def get_data_for_service(services):   
    data = []
    for service in services:
        data.append(
            (
                service.service_name,
                service.id, 
                service.service_classification.id,
                service.agency, 
                service.street, 
                service.city, 
                service.state,
                service.zipcode,
                service.country,
                service.url,
                service.contact_phone,
                service.contact_name,
                service.contact_email,
                service.contact_address
            )
        ) 
    return data    

def index(request):
    template = loader.get_template('servicediscovery/index.html')
    context = RequestContext(request)
    return render(request, "servicediscovery/index.html", {"ServicesClasses": get_data_for_service_class(Service_Classification.objects.all()), "Services": get_data_for_service(Service.objects.all())})

def log_hours_form(request):
    return render(request, "servicediscovery/log_hours.html")


def log_hours(request):
    pass

def search_hours(request):
    pass

def search_hours(request):
    classification = Service_Classification.objects.get(id=request.POST["id"])
    services = Serivce.objects.filter(service_classification=classification)
    return render(request, "servicediscovery/searchlisting.html", {"Servies": get_data_for_service(services)})

def new_student(request):
    Student(first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            year_graduation=request.POST["year_graduation"]
            ).save()
    return render(request, "servicediscovery/studentcreated.html", {"message": "Student Created!"})

def new_service_classification(request):
    Service_Classification(
        class_name=request.POST["class_name"]
    ).save()

def new_service(request):
    Service(
        service_classification=Service_Classification.objects.get(id=int(request.POST["service_classification"])),
        service_name=request.POST["service_name"],
        agency=request.POST["agency"],
        street=request.POST["street"],
        city=request.POST["city"],
        state=request.POST["state"],
        zipcode=request.POST["zipcode"],
        country=request.POST["country"],
        url=request.POST["url"],
        contact_phone=request.POST["contact_phone"],
        contact_name=request.POST["contact_name"],
        contact_email=request.POST["contact_email"],
        contact_address=request.POST["contact_address"]
    ).save()

def new_service_activity(request):
    Service_Activiy(
        service=Service.objects.get(id=int(request.POST["service"])),
        student=Student.objects.get(id=int(request.POST["student"])),
        start_time=request.POST["start_time"],
        end_time=request.POST["end_time"],
        hours=int(request.POST["hours"]),
        activiy_detail=request.POST["activiy_detail"],
        contact=request.POST["contact"],
        submitdate=timezone.now(),
    ).save()
