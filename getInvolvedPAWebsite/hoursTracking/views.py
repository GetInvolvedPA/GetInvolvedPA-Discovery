from django.shortcuts import render


from django.http import HttpResponse
from django.template import RequestContext, loader

#from hoursTracking.models import 


def index(request):
	template = loader.get_template('hoursTracking/index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))
	
