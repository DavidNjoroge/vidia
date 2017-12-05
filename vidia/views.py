from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Tag
from .forms import ProjectForm


# index page
def index(request):
    return render(request, 'index.html')

# project


@login_required(login_url='/accounts/login')
def submit_project(request):
    user = request.user

    new_project_form = ProjectForm(request.POST, request.FILES)
    if user.is_authenticated and new_project_form.is_valid():
        project = new_project_form.save(commit=False)
        project.user_id = user
        project.save()

        return redirect(index)

    else:
        new_project_form = ProjectForm(request.POST)

    return render(request, 'new_project.html', {"new_project_form": new_project_form})
