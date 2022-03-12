from django.shortcuts import render
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)

def project(request, pk):
    single_project = Project.objects.get(id=pk)
    tags = single_project.tags.all()
    return render(request, "projects/single-project.html", {"project": single_project, "tags": tags})