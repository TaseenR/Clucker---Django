from typing import BinaryIO
from django.shortcuts import redirect, render
from django.http import HttpResponse
from microblogs.forms import PostForm, SignUpForm
from microblogs.models import Post , User


def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                form.cleaned_data.get('username'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                bio=form.cleaned_data.get('bio'),
                password=form.cleaned_data.get('new_password')
            )
            return redirect('feed')
    else:
        form = SignUpForm()
    
    return render(request, 'signUp.html', {'form': form})

def feed(request):
    if request.method == 'Post':
        form = SignUpForm(request.POST)
    else:    
        form = PostForm()
    return render(request, 'feed.html', {'form':form})
