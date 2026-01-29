from django.shortcuts import render
from django.contrib.auth.models import User

from main.models import PreviousJob

# Create your views here.
def landing_page(request):
    users = User.objects.all()
    context = {
        "users": users,
        "jobs": PreviousJob.objects.all(),
    }
    return render(request, "main/landing.html", context)