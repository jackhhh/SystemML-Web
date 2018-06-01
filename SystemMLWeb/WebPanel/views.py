
from django.shortcuts import render

# Create your views here.

def index(request):
    # request.META.add('X-Frame-Options', ALLOWALL)
    return render(request, 'system/overview.html')