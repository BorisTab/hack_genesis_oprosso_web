import datetime

from django.db import models
from django.utils import timezone
from django import forms

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    need_people = models.IntegerField(default=0)
    cur_people = models.IntegerField(default=0)
    link = models.CharField(max_length=200)
    pkg_name = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200)

class RunTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()