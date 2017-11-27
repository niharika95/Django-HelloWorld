from django.conf.urls import url
from staticpages import views

urlpatterns = [
	url(r'^$', views.Home_page_view.as_view(), name='home'),
	url(r'^about', views.About_page_view.as_view(), name='about'),
]