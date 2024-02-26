from django.shortcuts import render,get_object_or_404
from .models import Post1
# Create your views here.



def post_list(request):
    posts = Post1.published.all()
    
    return render(request,'blog/list.html',{'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post1,id=id,status=Post1.Status.PUBLISHED)

    return render(request,'blog/detail.html',{'post': post})