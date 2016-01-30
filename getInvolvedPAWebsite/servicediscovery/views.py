from django.shortcuts import render


from django.http import HttpResponse
from django.template import RequestContext, loader

#from servicediscovery.models import


def index(request):
	template = loader.get_template('servicediscovery/index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

