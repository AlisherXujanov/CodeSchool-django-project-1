from django.shortcuts import render
from .forms import PostsForm

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
    return render(request, "posts.html")


def create_post(request):
    context = {
        "form": PostsForm()
    }
    return render(request, "create_post.html", context)


# request  =>  surov
# response =>  javob
