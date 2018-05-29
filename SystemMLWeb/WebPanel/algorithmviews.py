
from django.shortcuts import render

def kmeans(request):
    return render(request, 'algorithm/kmeans.html')