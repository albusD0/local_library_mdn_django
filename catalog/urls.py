from django.urls import include, re_path
from django.urls import path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^genres/$', views.GenreListView.as_view(), name='genres'),
    re_path(r'genre/(?P<pk>\d+)$', views.GenreDetailView.as_view(), name='genre-detail'),
]
