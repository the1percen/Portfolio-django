from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, JsonResponse
from .models import *
# Create your views here.

def home(request):
    project = Project.objects.all()
    tags = Tag.objects.all()
    context = {'project': project,'tags': tags}
    return render(request, 'home.html', context)

def contact(request):
    return render(request, "contact.html")

def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})

