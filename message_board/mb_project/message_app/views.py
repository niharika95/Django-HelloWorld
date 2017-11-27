from django.views.generic import ListView
from message_app import models

# Create your views here.

class Home_page_view(ListView):
	model = models.Post
	template_name = 'message_app/home.html'