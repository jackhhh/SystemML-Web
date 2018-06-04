from django.shortcuts import render
from api import tasks

# Create your views here.

def tasksubmit(request):
    info = request.POST.get()
    