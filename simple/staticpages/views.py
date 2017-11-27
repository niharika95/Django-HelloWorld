from django.views.generic import TemplateView

# Create your views here.
class Home_page_view(TemplateView):
	template_name = 'staticpages/home.html'

class About_page_view(TemplateView):
	template_name = 'staticpages/about.html'