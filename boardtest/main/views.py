from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def social_login_view(request):
    return render(request, "main/social_login.html")

def article_list(request):
    articles = Article.objects.all()
    return render(request, "main/article_list.html", {"articles": articles})


def article_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        id_name = request.user.username
        if id_name == "":
            id_name = "익명"

        Article.objects.create(title=title, content=content, id_name=id_name)
        return redirect("article_list")

    return render(request, "main/article_create.html")


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
    return render(request, "main/register.html", {"form": form})
