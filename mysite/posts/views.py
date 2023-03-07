from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostForms

p = Posts


def views_posts(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def create_post(request):
    form = PostForms(
        request.POST or None,
        files=request.FILES
    )
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=True)
            post.author = request.user
            post.save()
            return redirect('main')
    context = {
        "form": form,
    }
    return render(request, 'posts/create_post.html', context)