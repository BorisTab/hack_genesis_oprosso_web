import json
import datetime
import requests
import os

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from androguard.misc import AnalyzeAPK
from django.utils import timezone
# from .forms import ModelFormWithFileField
from .models import Task
from .counters import collect_counters

from glob import glob

def download_apk(url, output):
    r = requests.get(url, allow_redirects=True)
    with open(output, "wb") as out:
        out.write(r.content)
 
def get_package_name(filename):
    a, d, dx = AnalyzeAPK(filename)
    return a.get_package()

def decode_json(request):
    return json.loads(request.body.decode('utf-8'))

def convert_json(id, name, description, need_people, cur_people, link, package_name, pub_date):
    inf_task = {'task_id' : id, 'name' : name, 'description' : description, 'num_of_people' : need_people, 'cur_people' : cur_people,'file_ref' : link, 'pkg_name' : package_name, 'date' : pub_date}
    return JsonResponse(inf_task)

@csrf_exempt
def add_task(request):
    new_task = decode_json(request)
    download_apk(new_task['file_ref'], 'app.apk')
    package_name = get_package_name('app.apk')
    new = Task(name=new_task['name'], description=new_task['description'], need_people=new_task['num_of_people'], cur_people=0, link=new_task['file_ref'], pkg_name=package_name, pub_date=datetime.datetime.now().strftime('%d %B, %Y'))
    new.save()
    return JsonResponse({"task_id" : new.task_id})

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

def show_counters_table(request):
    views = glob('telemetry/*.xml')
    counters = collect_counters(views, 'telemetry/event-log.txt')
    counter_dicts = []
    
    for key in counters.keys():
        counter_dicts.append({'id' : str(key), 'type': counters[key]['type'][0], 'label': counters[key]['label'], 'events': counters[key]['events']})
    return JsonResponse({'counters' : counter_dicts})


def render_page(request):
    return render(request, 'frontend/index.html')
