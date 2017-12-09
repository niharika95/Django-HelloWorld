from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog_app.models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(ListView):
	model = Post
	template_name = 'blog_app/post_list.html'
	context_object_name = 'postList'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'blog_app/post_detail.html'
	context_object_name = 'postDetail'

class BlogCreateView(CreateView):
	model = Post
	template_name = 'blog_app/post_new.html'
	fields = '__all__'

class BlogUpdateView(UpdateView):
	model = Post
	template_name = 'blog_app/post_edit.html'
	fields = ['title', 'text']

class BlogDeleteView(DeleteView):
	model = Post
	template_name = 'blog_app/post_delete.html'
	success_url = reverse_lazy('post_list')