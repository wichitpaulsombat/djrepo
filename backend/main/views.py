from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import *
from .serializers import *

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class PreviousJobViewSet(viewsets.ModelViewSet):
    queryset = PreviousJob.objects.all()
    serializer_class = PreviousJobSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer    

# Create your views here.
def landing_page(request):
    users = User.objects.all()
    context = {
        "users": users,
        "jobs": PreviousJob.objects.all(),
    }
    return render(request, "main/landing.html", context)