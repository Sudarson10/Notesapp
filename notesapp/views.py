from django.shortcuts import render,redirect
from .models import Task
from .forms import Taskform 
def homepage(request,title=None):
    form=Task.objects.all()
    c=Task.objects.only('id').count()
    data = {"all":form, "count":c}
    return render(request,"homepage.html",data)
def create(request):
    form=Taskform()
    if(request.method=='POST'):
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    data={'form':form}
    return render(request,'create.html',data)
def update(request,pk):
    form1=Task.objects.get(id=pk)
    form=Taskform(instance=form1)
    if(request.method=='POST'):
        form=Taskform(request.POST,instance=form1)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    data={'form':form}
    return render(request,'update.html',data)
def delete(request,pk):
    form=Task.objects.get(id=pk)
    if(request.method=='POST'):
        form.delete()
        return redirect("homepage")
    data={'form':form}
    return render(request,'delete.html',data)