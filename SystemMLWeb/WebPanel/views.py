
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'system/overview.html')

def kmeans(request):
    return render(request, 'algorithm/kmeans.html')