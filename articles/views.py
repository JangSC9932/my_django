from django.shortcuts import render, redirect

from .models import Article


# Create your views here.
def index(request):
    return render(request, "index.html")


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
    return render(request, "hello.html", context)


def data_throw(request):
    return render(request, "data_throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {
        "message": message
    }
    return render(request, "data_catch.html", context)


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
    return render(request, "articles.html", context)


# 글 상세 페이지
def detail_article(request, article_id):
    context = {
        "article": Article.objects.get(id=article_id)
    }
    return render(request, "detail.html", context)


# 글 작성 페이지
def new_articles(request):
    return render(request, "new.html")


# 글 작성 요청
def create_article(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    article = Article.objects.create(title=title, content=content)
    return redirect("detail_article", article_id=article.id)


# 글 수정
def update_article(request, article_id):
    # 수정 페이지
    if request.method == "GET":
        context = {
            "article": Article.objects.get(id=article_id)
        }
        return render(request, "update.html", context)
    # 수정 요청
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.get(id=article_id)
        article.title = title
        article.content = content
        article.save()
        return redirect("detail_article", article_id=article_id)


# 글 삭제
def delete_article(request, article_id):
    Article.objects.get(id=article_id).delete()
    return redirect("articles")
