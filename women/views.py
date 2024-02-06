from typing import Any
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, logout,login
# Create your views here.
from .models import *
from .forms import *

list_data_about = ['About1', 'About2','About3']


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'records'
    extra_context = {'title':'Main'}# extra_context - only for static data

    #manage data dynamic 
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['menu'] = list_data_about
        context['title'] = 'Main'

        return context
    #Get only that we want to see
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

class ShowCategory(ListView):
    model = Category
    template_name = 'women/index.html'
    context_object_name = 'records'
    allow_empty = False

    def get_queryset(self):
        print(Women.objects.filter(cat_id=1))
        print(self.kwargs['cat_id'])
        return Women.objects.filter(cat_id=self.kwargs['cat_id'],is_published=True)
    

class ShowPost(DetailView): 
    model = Women
    template_name = 'women/post.html'
    #slug_url_kwarg = 'slug_name'
    context_object_name = 'post_data'

class AddPage(LoginRequiredMixin,CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    #success_url = reverse_lazy('home') ???

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'women/login.html'
    success_url = reverse_lazy('home')
    
    def get_success_url(self):
        return reverse_lazy('home')

@login_required
def about(request):
    return render(request,'women/about.html', {'title':'Text Title About','list_data':list_data_about})

def logout_user(request):
    logout(request)
    return redirect('login')

def women(request):
    print(request)
    return HttpResponse("WomenPage")

def cat(request,catid):
    print(f"catid : {int(catid)}")
    if int(catid) > 100:
        raise Http404()
    if int(catid) == 99:
        return redirect('index')
        # or use return redirect('/', permanent=True)
    
    return HttpResponse(f"Cats:{catid}")

###Example code
# def addpage(requset):
#     if requset.method == 'POST':
#         form = AddPostForm(requset.POST,requset.FILES)
#         if form.is_valid():
#                 form.save()
#                 return redirect('home')
#     else:
#         form = AddPostForm()

#     return render(requset,'women/addpage.html',{'form':form})

def contact(requset):
    return HttpResponse(f"contact")

def pageNotFound(requet,exception):
    return HttpResponseNotFound("Not Found")