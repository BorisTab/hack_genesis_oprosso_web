# from django.shortcuts import render
import json

from django.http import HttpResponse

def decode_json(request):
    return json.loads(request.body.decode('utf-8'))

def convert_json(id, name, description, people, link, pub_date):
    inf_task = {'id' : task.id, 'name' : task.name, 'description' : task.description, 'num_of_people' = task.people, 'file_ref' = task.link, 'date' : task.pub_date}
    return JsonResponse(json.dumps(inf_task))

def add_task(request):
    new_task = decode_json(request)
    new = Task(name=new_task['name'], description=new_task['description'], people=new_task['num_of_people'], link=new_task['file_ref'], pub_date=timezone.now())
    new.save()

def show_all_tasks(request):
    all_tasks = Task.objects.all()
    all_tasks_json = []

    for task in all_tasks:
        all_tasks_json.append(convert_json(task.id, task.name, task.description, task.people, task.link, task.pub_date))
    JsonResponse(all_tasks_json)

def show_task(request):
    task_id = decode_json(request)
    task = Task.objects.get(id=task_id)
    inf_task = {'id' : task.id, 'name' : task.name, 'description' : task.description, 'num_of_people' = task.people, 'file_ref' = task.link, 'date' : task.pub_date}
    return JsonResponse(json.dumps(inf_task))
