from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Idea

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def ideas_index(request):
    ideas = Idea.objects.all()
    return render(request, 'ideas/index.html', {'ideas':ideas})

def idea_detail(request, idea_id):
    idea = Idea.objects.get( id=idea_id)
    return render(request,'ideas/detail.html', {'idea':idea})

class IdeaCreate(CreateView, ):
  model = Idea
  fields = '__all__'

class IdeaUpdate(UpdateView, ):
  model = Idea
  fields = '__all__'

class IdeaDelete(DeleteView):
  model = Idea
  success_url = '/ideas/'