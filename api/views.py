from django.shortcuts import render
import json
import datetime

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Task

def decode_json(request):
    return json.loads(request.body.decode('utf-8'))

def convert_json(id, name, description, num_people, cur_people, link, package_name, pub_date):
    inf_task = {'task_id' : id, 'name' : name, 'description' : description, 'num_of_people' : num_people, 'cur_people' : cur_people,'file_ref' : link, 'pkg_name' : package_name, 'date' : pub_date}
    return JsonResponse(inf_task)

@csrf_exempt
def add_task(request):
    new_task = decode_json(request)
    # function for package_name
    new = Task(name=new_task['name'], description=new_task['description'], need_people=new_task['num_of_people'], cur_people=new_task['cur_people'], link=new_task['file_ref'], pkg_name='package_name', pub_date=datetime.datetime.now().strftime('%d %A %Y'))
    new.save()
    return HttpResponse(200)

def show_all_tasks(request):
    all_tasks = Task.objects.all()
    all_tasks_json = []

    for task in all_tasks:
        all_tasks_json.append(convert_json(task.task_id, task.name, task.description, task.need_people, task.cur_people, task.link, task.pkg_name, task.pub_date))
        
    JsonResponse(all_tasks_json)
  

def show_task(request, task_id):
    task = Task.objects.get(task_id=task_id)
    inf_task = convert_json(str(task.task_id), task.name, task.description, str(task.need_people), str(task.cur_people), task.link, task.pkg_name, str(task.pub_date))
    return inf_task

def render_page(request):
    return render(request, 'frontend/index.html')