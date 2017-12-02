from django.views.generic import ListView, DetailView
from blog_app.models import Post

# Create your views here.
class BlogListView(ListView):
	model = Post
	template_name = 'blog_app/post_list.html'
	context_object_name = 'postList'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'blog_app/post_detail.html'
	context_object_name = 'postDetail'