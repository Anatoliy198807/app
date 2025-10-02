from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.

def index_view(request):
    return render(request, 'index.html') 
    #return HttpResponse("Главная страница")
    
def post_list_view(request):
    posts = Post.objects.all()

    return render(request, 'post_list.html', {'posts':posts})    

def post_detail_view(request, post_id):
    #post = Post.objects.get(id=post_id)
    post =get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post':post})