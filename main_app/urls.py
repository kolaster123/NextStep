from django.urls import path 
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ideas/', views.ideas_index, name ='ideas-index'),
    path('ideas/<int:idea_id>/', views.idea_detail, name= 'idea-detail'),
    path('ideas/create/', views.IdeaCreate.as_view(), name='idea-create'),
    path('ideas/<int:pk>/update/', views.IdeaUpdate.as_view(), name='idea-update'),
    path('ideas/<int:pk>/delete/', views.IdeaDelete.as_view(), name='idea-delete')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  