from django.http import HttpResponse
from django.shortcuts import render

#def hello(request):
#    return HttpResponse("Hello world ! ")


from django.shortcuts import render,render_to_response

import json

def ajax_list(request):
    a = range(100)
    return HttpResponse(json.dumps(a), content_type='application/json')

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')


def sixDegree(request):
    return render_to_response('web.html')

def index(request):
    return render(request, 'index.html')


