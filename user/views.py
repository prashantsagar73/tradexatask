from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,"user/home.html",context)

def about(request):
    return render(request,"about.html")


def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' Your account has been created! Now you are able to login.')
            return redirect('user/login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f' Your account has been Updated!')
        return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'user/profile.html', context)


# for listing the post to get their id
class PostListView(ListView):
    model = Post
    template_name = "user/home.html"  #<app>/<model> _ <viewtype>.html
    context_object_name = 'posts'
    ordering =['-date_time']

class PostDetailView(DetailView):
    model = Post
    template_name = 'user/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields =['title','content']
    template_name = 'user/post_forms.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields =['title','content']
    template_name = 'user/post_forms.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'user/post_confirm_delete.html'
    success_url= "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


