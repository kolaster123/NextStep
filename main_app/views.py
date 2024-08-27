from django.shortcuts import render
from .models import Idea

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def ideas_index(request):
    ideas = Idea.objects.all()
    return render(request, 'ideas/index.html', {'ideas':ideas})

def idea_detail(request, cat_id):
    idea = Idea.objects.get(id = cat_id)
    return render(request,'ideas/index.html', {'Idea':Idea})




