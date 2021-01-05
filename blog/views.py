from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def like_post(request, pk):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    liked= False
    #disliked= False

    if not post.likes.filter(id= request.user.id).exists() and post.dislikes.filter(id= request.user.id).exists():
        post.dislikes.remove(request.user)
        post.likes.add(request.user)
        liked= False
    elif post.likes.filter(id= request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    elif not post.dislikes.filter(id= request.user.id).exists():
        post.likes.add(request.user)
        liked= True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def dislike_post(request, pk):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    disliked= False
    #liked=False
    if not post.dislikes.filter(id= request.user.id).exists() and post.likes.filter(id= request.user.id).exists():
        post.likes.remove(request.user)
        post.dislikes.add(request.user)
        liked= False
    elif post.dislikes.filter(id= request.user.id).exists():
        post.dislikes.remove(request.user)
        disliked=False
    elif not post.likes.filter(id= request.user.id).exists():
        post.dislikes.add(request.user)
        disliked= True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def home(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model= Post
    template_name= 'blog/home.html'
    context_object_name= 'posts'
    ordering= ['-date_posted']
    paginate_by= 5

class UserPostListView(ListView):
    model= Post
    template_name= 'blog/user_post.html'
    context_object_name= 'posts'
    paginate_by= 5
    
    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class UserOwnPostListView(ListView):
    model= Post
    template_name= 'blog/logged_in_user_post.html'
    context_object_name= 'posts'
    paginate_by= 5
    
    def get_queryset(self):
        user=get_object_or_404(User, username=self.request.user)
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model= Post
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data()
        post_obj= get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes=post_obj.total_likes()
        post_obj= get_object_or_404(Post, id=self.kwargs['pk'])
        total_dislikes=post_obj.total_dislikes()
        context["total_likes"]=total_likes
        context["total_dislikes"]=total_dislikes
        return context

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        """
        Sets the author of the post to the current logged in user.
        """
        
        form.instance.author= self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        """
        Check whether the user trying to update the post is the author of the post or not.
        """

        post=self.get_object() #Gets the current post that we are updating.
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Post
    success_url= "/"

    def test_func(self):
        """
        Check whether the user trying to update the post is the author of the post or not.
        """

        post=self.get_object() #Gets the current post that we are updating.
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

def announcement(request):
    return render(request,'blog/announcements.html',)