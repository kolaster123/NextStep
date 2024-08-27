from django.urls import path 
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ideas/', views.ideas_index, name ='ideas-index'),
    path('ideas/<int:idea_id>/', views.idea_detail, name= 'cat-detail'),
]