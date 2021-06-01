from userprofile.models import Userprofile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .models import Team

# Create your views here.

@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            team = Team.objects.create(title=title, created_by=request.user)
            team.members.add(request.user)
            team.save()

            userprofile = request.user.userprofile
            userprofile.active_team_id = team.id
            userprofile.save()

            return redirect('myaccount')
    
    return render(request, 'teams/add.html')