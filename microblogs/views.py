from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model,login,logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from microblogs.forms import PostForm, SignUpForm, LogInForm
from microblogs.models import Post , User


def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('feed')
    else:
        form = SignUpForm()
    
    return render(request, 'signUp.html', {'form': form})

def feed(request):
    model = Post
    posts = Post.objects.filter(author=request.user).order_by()
    return render(request, 'feed.html', {'posts':posts})

def show_user(request, user_id):
    users = get_user_model().objects.get(pk = user_id)
    posts = Post.objects.filter(author_id = user_id).order_by()
    return (render(request, 'show_user.html', {'user':users}))

def user_list(request):
    model = get_user_model()
    users = get_user_model().objects.all()
    return render(request, 'user_list.html', {'users':users})

def new_post(request):
    model = Post
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            posts = Post.objects.all().filter(author = request.user)
            user = form.save(request.user)
            return redirect('feed')
    return render(request, 'new_post.html',{'form':form})

    
def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
            messages.add_message(request, messages.ERROR, 'The credentials provided were invalid')
    form = LogInForm()
    return render(request, 'log_in.html', {'form':form})

def log_out(request):
    logout(request)
    return(redirect('home'))

def edit_feed(request):

    return render(request, 'edit_feed.html')


    