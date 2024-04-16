from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('data_throw/', views.data_throw, name='data_throw'),
    path('dtaa_catch/', views.data_catch, name='data_catch'),
    path('', views.articles, name='articles'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_id>/', views.detail_article, name='detail_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
    path('update/<int:article_id>/', views.update_article, name='update_article'),
]