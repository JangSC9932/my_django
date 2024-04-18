from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import ArticleForm, CommentForm
from .models import Article, Comment


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
    article = get_object_or_404(Article, pk=article_id)
    comment_form = CommentForm()
    comments = article.comments.all()
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments
    }
    return render(request, "articles/detail.html", context)


@login_required
# 글 작성
def create_article(request):
    if request.method == "GET":
        context = {
            "form": ArticleForm()
        }
        return render(request, "articles/new.html", context)
    else:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("articles:detail_article", article.id)


# 글 수정
@login_required
def update_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # 수정 페이지
    if request.method == "GET":
        if article.author == request.user:
            context = {
                "article": article,
                "form": ArticleForm()
            }
            return render(request, "articles/update.html", context)
        else:
            return redirect("articles:detail_article", article_id)
    # 수정 요청
    else:
        if article.author == request.user:
            ArticleForm(request.POST, instance=article).save()
        return redirect("articles:detail_article", article_id)


# 글 삭제
@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.author == request.user:
        article.delete()
    return redirect("articles:articles")


# 댓글
@require_POST
@login_required
def comment_create(request, article_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article_id = article_id
        comment.save()
    return redirect("articles:detail_article", article_id)


# 댓글 삭제
@login_required
def comment_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
    return redirect("articles:detail_article", article_id)


