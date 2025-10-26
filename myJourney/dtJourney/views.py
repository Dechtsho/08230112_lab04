from django.shortcuts import render, get_object_or_404
from .models import Profile, LearningEntry

# Create your views here.

def index(request):
    entries = LearningEntry.objects.all().order_by('-date')
    return render(request, 'index.html', {'entries': entries})

def about_me(request):
    profile = Profile.objects.first()
    return render(request, 'aboutme.html', {'profile': profile})
