from django.shortcuts import render, redirect
from .forms import PostsForm
from .models import Posts

# Create your views here.


def home(request):
    text = "This is test text"
    context = {"text": text}
    return render(request, "home.html", context)


def about(request):
    text = "This is test text for ABOUT PAGE"
    context = {"text": text}
    return render(request, "about.html", context)


def posts(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, "posts.html", context)


def create_post(request):
    context = {
        "form": PostsForm()
    }
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("posts")
    return render(request, "create_post.html", context)


# request  =>  surov
# response =>  javob
