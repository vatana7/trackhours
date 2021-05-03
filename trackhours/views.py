from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

def frontpage(request):
    return render(request, 'trackhours/frontpage.html')

def privacy(request):
    return render(request, 'trackhours/privacy.html')

def terms(request):
    return render(request, 'trackhours/terms.html')

def plans(request):
    return render(request, 'trackhours/plans.html')
# Create your views here.
