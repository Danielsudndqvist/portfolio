from django.shortcuts import render
from .models import Project, Technology, Education, WorkExperience

def project_list(request):
    projects = Project.objects.all().order_by('-created_date')  # Changed from created_at to created_date
    return render(request, 'projects/project_list.html', {'projects': projects})

def home(request):
    featured_projects = Project.objects.filter(featured=True).order_by('-created_date')
    technologies = Technology.objects.all()
    educations = Education.objects.all().order_by('-end_date', '-start_date')
    work_experiences = WorkExperience.objects.all().order_by('-end_date', '-start_date')
    
    return render(request, 'projects/home.html', {
        'featured_projects': featured_projects,
        'technologies': technologies,
        'educations': educations,
        'work_experiences': work_experiences,
    })
    