#from django import http
import django

def home(request):
    return django.http.HttpResponse('Hello JBD! Django version:' + django.get_version())
