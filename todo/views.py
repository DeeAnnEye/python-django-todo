# from django.shortcuts import render

from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

from .models import Task

def index(request):
    return render(request, 'todo/index.html')

def tasks(request):
    todo_list = Task.objects.order_by('task_text')
    # for e in Task.objects.all():
    #   print(e.task_date)
    # template = loader.get_template('todo/index.html')
    # context = {
    #     'todo_list': todo_list,
    # }
    # return HttpResponse(template.render(context, request))
    # print(request.POST)
    context = {'todo_list': todo_list}
    return render(request, 'todo/tasks.html', context)

