#Import Django

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Import models

from .models import Project
from teams.models import Team

# Create your views here.

@login_required
def projects(request):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)
    projects = team.projects.all()

    return render(request, 'project/project.html', {'team': team, 'projects': projects})