from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^posts/(?P<slug>[\w\-]+)$', views.PostView.as_view(), name='posts'),
]



#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#    url(r'^books/$', views.BookListView.as_view(), name='books'),
#    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
#    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
#    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
#]
