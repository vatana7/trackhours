from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from teams.models import Team
# Create your views here.

@login_required
def projects(request):
    
    return render(request, 'project/projects.html')