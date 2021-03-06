from django.urls import path

from . import views

urlpatterns = [
    #ex: /api/
    path('', views.render_page, name='render_page'),
    # ex: /api/5/
    path('<int:task_id>/', views.show_task, name='show_task'),
    # ex: /api/add/
    path('add/', views.add_task, name='add_task'),
    path('counters/', views.show_counters_table, name='show_counters_table')
    # ex: /api/5/vote/
    #path('<int:task_id>/vote/', views.vote, name='vote'),
]
