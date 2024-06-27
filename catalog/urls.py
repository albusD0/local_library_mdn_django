from django.urls import include, re_path
#from django.urls import path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^author/$', views.AuthorListView.as_view(), name='authors'),
]
