from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm
# Create your views here.

def index_view(request):
    posts = Post.objects.all()
    return render(request, 'mainpage/index.html', {'posts':posts}) 
    #return HttpResponse("Главная страница")
    
def post_list_view(request):
    posts = Post.objects.all()

    return render(request, 'mainpage/post_list.html', {'posts':posts})    

def post_detail_view(request, post_id):
    #post = Post.objects.get(id=post_id)
    post =get_object_or_404(Post, id=post_id)
    return render(request, 'mainpage/post_detail.html', {'post':post})

@login_required
def create_post_view(request):
    if request.method == "GET":
        form= PostForm()

        context = {
            'form':form,
            'title':'Создать пост',
            'submit_bytton_text':'Создать'
        }

        return render(request, 'mainpage/post_form.html', context)
    
    if request.method == "POST":
        form = PostForm(request.POST)        

        if form.is_valid():
            post = form.save(commit=False)

            post.author=request.user
            post.save()
            
            return redirect('mainpage:post_detail', post_id=post.id)
        
def edit_post_view(request, post_id):
    post =get_object_or_404(Post, id=post_id)

    if request.method == "GET":
        form = PostForm(instance=post)

        context = {
            'form':form,
            'title':'Редактировать пост',
            'submit_bytton_text':'Обновить'
        }

        return render(request, 'mainpage/post_form.html', context)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)    


        if form.is_valid():
            form.save()
            return redirect('mainpage:post_detail', post_id=post.id)
        
def  delete_post_view(request, post_id):
    print("____________")
    print(request)
    print("____________")
    post =get_object_or_404(Post, id=post_id)

    post.delete()   

    return redirect('mainpage:post_list')