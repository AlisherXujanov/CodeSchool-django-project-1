from django.shortcuts import render

# Create your views here.


def home(request):
    text = "This is test text"
    context = {"text": text}
    return render(request, "home.html", context)


def about(request):
    text = "This is test text for ABOUT PAGE"
    context = {"text": text}
    return render(request, "about.html", context)


# request  =>  surov
# response =>  javob
