from django.shortcuts import redirect, render
from TodoApp.models import Todo
from TodoApp.forms import TodoForm

# Create your views here.
def index(request):
    todo_list=Todo.objects.order_by('id')
    
    form=TodoForm()
    dict={
        'todo_list':todo_list,
        'form':form
    }  
    return render(request,'TodoApp/index.html', context=dict)

def addTodo(request):
    if request.method=='POST':
        #print(request.POST['text'])
        form=TodoForm(request.POST)
        if form.is_valid():
            new_todo=Todo(text=request.POST['text'])
            new_todo.save()
    return redirect('index')

def completeTodo(request, todo_id):
    todo=Todo.objects.get(pk=todo_id)
    todo.complete=True
    todo.save()
    return redirect('index')

def deleteCompletedTodo(request):
    Todo.objects.filter(complete=True).delete()
    
    return redirect('index')