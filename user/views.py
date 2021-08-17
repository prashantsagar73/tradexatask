from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")


def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('Blog_home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})