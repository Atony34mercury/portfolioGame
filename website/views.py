from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings":Meeting.objects.all()})

def date(request):
    return HttpResponse(f"Server time is {datetime.now()}")

def about(request):
    return HttpResponse("I am 25 year old")