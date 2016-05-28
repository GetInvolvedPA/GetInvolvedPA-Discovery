#!/usr/bin/env python2
# This script populates the database with a preset list of classifications
# and services from a CSV file (downloaded from the Google spreadsheet).
#
# See https://docs.djangoproject.com/en/1.9/howto/custom-management-commands/#module-django.core.management
# for help on writing Django custom commands.
#
# Usage:
# python manage.py populate_database

from django.core.management.base import BaseCommand, CommandError
from servicediscovery.models import *

service_classifications = ['Education',
                           'Sports',
                           'Seniors/Disabled',
                           'Animals/Environment',
                           'Civic Engagement',
                           'Home Construction',
                           'Health Care/Safety',
                           'Humanitarianism',
                           'Food/Shelter']

class Command(BaseCommand):
    help = 'Populate the database with a preset list of classifications'

    def handle(self, *args, **options):
        # now do the things that you want with your models here
        current_services = [i.class_name for i in Service_Classification.objects.all()]
        for service_classification in service_classifications:
            if service_classification not in current_services:
                s = Service_Classification(class_name=service_classification)
                s.save()


