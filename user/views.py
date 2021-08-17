from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

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
            messages.success(request, f' Your account has been created! Now you are able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request,'profile.html')