from django.shortcuts import render,get_object_or_404
from .models import Post1
from django.core.paginator import Paginator

# Create your views here.



def post_list(request):
    post_list = Post1.published.all()
 
    paginator = Paginator(post_list,2)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)


    
    return render(request,'blog/list.html',{'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post1,id=id,status=Post1.Status.PUBLISHED)

    return render(request,'blog/detail.html',{'post': post})