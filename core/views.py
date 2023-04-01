from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    post = Company.objects.all()
    return render(request, 'index.html', {'post':post})

def add(request):
    form = CompanyForm(request.POST)
    if request.method == 'POST':
        if  form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CompanyForm()
    return render(request, 'add.html', {'form':form})

def delete(request, id):
    delete_post = Company.objects.get(id=id)
    delete_post.delete()
    return redirect('home')

def edit(request, id):
    post = Company.objects.get(id=id)

    return render(request, 'update.html', {'post':post})