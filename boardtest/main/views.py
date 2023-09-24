from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm


# Create your views here.
def social_login_view(request):
    return render(request, "social_login.html")


def article_list(request):
    # DB 불러오기
    datas = Article.objects.all()
    return render(request, "article_list.html", {"datas": datas})


def article_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        id_name = request.user.username
        if id_name == "":
            id_name = "익명"

        Article.objects.create(title=title, content=content, id_name=id_name)
        return redirect("article_list")

    return render(request, "article_create.html")


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("article_list")
        else:
            form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_request(request):
    logout(request)
    return redirect("article_list")


def register_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("article_list")
    return render(request, "register.html", {"form": form})
