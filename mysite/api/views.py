from django.shortcuts import render
import json
import datetime

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Task

def decode_json(request):
    return json.loads(request.body.decode('utf-8'))

def convert_json(id, name, description, people, link, pub_date):
    inf_task = {'task_id' : id, 'name' : name, 'description' : description, 'num_of_people' : people, 'file_ref' : link, 'date' : pub_date}
    return JsonResponse(inf_task)

@csrf_exempt
def add_task(request):
    new_task = decode_json(request)
    new = Task(name=new_task['name'], description=new_task['description'], people=new_task['num_of_people'], link=new_task['file_ref'], pub_date=timezone.now())
    new.save()

def show_all_tasks(request):
    all_tasks = Task.objects.all()
    all_tasks_json = []

    for task in all_tasks:
        all_tasks_json.append(convert_json(task.task_id, task.name, task.description, task.people, task.link, task.pub_date))
        
    JsonResponse(all_tasks_json)
  

def show_task(request, task_id):
    # id_of_task = decode_json(request)
    task = Task.objects.get(task_id=task_id)
    inf_task = convert_json(str(task.task_id), task.name, task.description, str(task.people), task.link, str(task.pub_date))
    return inf_task

def render_page(request):
    return render(request, 'frontend/index.html')