from django.conf.urls import url
from message_app import views

urlpatterns = [
	url(r'^$', views.Home_page_view.as_view()),
]