from django.urls import path

from . import views

urlpatterns = [
    #ex: /api/
    # path('', views.index, name='index'),
    # ex: /api/5/
    path('<int:task_id>/', views.show_task, name='show_task'),
    
    # ex: /poapills/5/results/
    path('add/', views.add_task, name='add_task'),
    # ex: /api/5/vote/
    #path('<int:task_id>/vote/', views.vote, name='vote'),
]