from django.shortcuts import render, redirect
from django.http import HttpResponse    # gets the response 

from .models import *  # imports all the items in models file
from .forms import *   # import form to views and then to the template (context) -> goes to list.html

# Create your views here.

# view that lets us add item/tasks
def index(request):
    tasks = Task.objects.all()  # gets all the objects in the Task class from models.py
    form = TaskForm()  # name of the form we created in forms.py and pass it to the template (context) -> goes to list.html
    
    if request.method == 'POST':   # if the request method is POST
        form = TaskForm(request.POST)   # passes the post method and save the form
        if form.is_valid():    # if the form with the post method is valid, then save it
            form.save()
        return redirect('/')   # it it's valid, redirect to the home page (redirect to the same url path)

    context = {'tasks': tasks, 'form': form}    # gets all the objects in a dict to pass it into the render func
    return render(request, 'tasks/list.html', context)  # renders the message from the templates/tasks folder from the list.html file -> update it in urls.py

# view that lets us make edits to the tasks
def updateTask(request, pk):  # pk is a dynamic url path (primary key in the url)
    task = Task.objects.get(id=pk)  # Task from the class in models.py and id is the url pattern (pk) -> update url pattern from the tasks app

    form = TaskForm(instance=task)   # instance prefills the form the the current info (from forms.py, instance is the task created)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # add request.POST (updates the new data), but we also need instance to still update it
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}  # context passed to update_task.html template 
    
    return render(request, 'tasks/update_task.html', context)  # returns the template called update_task.html

# view that lets the customer delete the task
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':   # if it's post then delete the item 
        item.delete()
        return redirect('/')   # redirect back to homepage (list.html)

    context = {'item': item}  # pass the item
    return render(request, 'tasks/delete.html', context)  # update it in urls.py from the app
