from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def todo_list(request):
    todos=Todo.objects.all()
    return render(request,'index.html',{'todos':todos})

def create_todo(request):
    if request.method == "POST":
        Title=request.POST.get('Title')
        Description=request.POST.get('Description')
        Todo.objects.create(Title=Title,Description=Description)
    return redirect('todo_list')


def complete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed=True
    todo.save()
    return redirect('todo_list')

def delete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    todo.save()
    return redirect('todo_list')



