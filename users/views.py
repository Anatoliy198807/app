from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == "GET":
        form = CustomUserCreationForm()
    
        return render(request, 'register.html', {"form":form})
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            
            print(form.fields['password1'].error_messages)
            return render(request, 'register.html', {"form":form})
        
def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()

        return render(request, 'login.html', {'form':form})
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():
            user = form.get_user()
            print(user)
            print(user.id)
            login(request, user)
            return redirect('post_list')
        else:
            return render(request, 'login.html', {"form":form})
        
def logout_view(request):
    print()
    logout(request)    
    return redirect('post_list')

def edit_profil_view(request):
    if request.method == "GET":
        form = CustomUserCreationForm()

        return render(request, 'register.html', {"form":form})
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            
            return render(request, 'register.html', {"form":form})