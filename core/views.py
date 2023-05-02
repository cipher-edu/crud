from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse
from  django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import *
from .forms import *
# Create your views here.

class SingupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserform
    def get_success_url(self):
        return reverse('home')
# @login_required
def home(request):
    post_list = Company.objects.all()
    paginator = Paginator(post_list, 1) # Show 10 posts per page
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post = paginator.page(paginator.num_pages)
    context = {
        'post_list':post_list,
        'post':post
    }
    return render(request, 'index.html',context=context)

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

def editpost(request, id):
    name = request.POST['name']
    about = request.POST['name']
    taxrir = Company.objects.get(id=id)
    taxrir.name = name
    taxrir.about = about
    return redirect('home')