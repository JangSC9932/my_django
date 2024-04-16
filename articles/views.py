from django.shortcuts import render, redirect

from .forms import ArticleForm
from .models import Article


# Create your views here.
def index(request):
    return render(request, "articles/index.html")


def users(request):
    return render(request, "users.html")


def hello(request):
    name = "Jang"
    tags = ["python", "django", "html", "css"]
    books = ['해변의 카프카', "코스모스", "백설공주", "어린왕자"]

    context = {
        "name": name,
        "tags": tags,
        "books": books,
    }
    return render(request, "articles/hello.html", context)


def data_throw(request):
    return render(request, "articles/data_throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {
        "message": message
    }
    return render(request, "articles/data_catch.html", context)


def profile(request, username):
    context = {
        "username": username
    }
    return render(request, "profile.html", context)


# 글 목록 페이지
def articles(request):
    context = {
        "articles": Article.objects.all().order_by("-created_at")
    }
    return render(request, "articles/articles.html", context)


# 글 상세 페이지
def detail_article(request, article_id):
    context = {
        "article": Article.objects.get(id=article_id)
    }
    return render(request, "articles/detail.html", context)


# 글 작성
def create_article(request):
    if request.method == "GET":
        context = {
            "form": ArticleForm()
        }
        return render(request, "articles/new.html", context)
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail_article", article.id)


# 글 수정
def update_article(request, article_id):
    article = Article.objects.get(id=article_id)
    # 수정 페이지
    if request.method == "GET":
        context = {
            "article": article,
            "form": ArticleForm()
        }
        return render(request, "articles/update.html", context)
    # 수정 요청
    else:
        ArticleForm(request.POST, instance=article).save()
        return redirect("articles:detail_article", article_id)


# 글 삭제
def delete_article(request, article_id):
    Article.objects.get(id=article_id).delete()
    return redirect("articles:articles")
