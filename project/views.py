from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from teams.models import Team
from .models import Project
# Create your views here.

@login_required
def projects(request):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)
    projects = team.projects.all()

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            project = Project.objects.create(team=team, title=title, created_by=request.user)

            messages.info(request, 'The project was added!')

            return redirect('project:projects')

    return render(request, 'project/projects.html', {'team': team, 'projects': projects})

@login_required
def project(request, project_id):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)
    project = get_object_or_404(Project, team=team, pk=project_id)

    return render(request, 'project/project.html', {'team': team, 'project': project})
