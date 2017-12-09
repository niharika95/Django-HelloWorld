#from django.conf.urls import url
from django.urls import path
from blog_app import views

urlpatterns = [
	path('', views.BlogListView.as_view(), name='post_list'),
	path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
	path('post/new', views.BlogCreateView.as_view(), name='post_new'),
	path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
	path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
]


# urlpatterns = [
# 	url(r'^$', views.BlogListView.as_view(), name = 'post_list'),
# 	url(r'^post/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name = 'post_detail'),
# 	url(r'^post/new/$', views.BlogCreateView.as_view(), name = 'post_new'),
# ]