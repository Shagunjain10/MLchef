from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from myblog.models import Post

def home(request):
	context = {
        'posts': Post.objects.all()
    }
	return render(request,'myblog/home.html',context)

class Post_ListView(ListView):
	"""docstring for Post_ListView"""
	model = Post
	template_name = 'myblog/home.html' 
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5
	# myblog/post_list.html
	# def __init__(self, arg):
	# 	super(Post_ListView, self).__init__()
	# 	self.arg = arg
		
class userPost_ListView(ListView):
	"""docstring for Post_ListView"""
	model = Post
	template_name = 'myblog/user_post.html' 
	context_object_name = 'posts'
	paginate_by = 2
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')



class Post_DetailView(DetailView):
	model = Post

class Post_DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post

	success_url = '/'	# home page, when post is deleted
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class Post_CreateView(LoginRequiredMixin,CreateView):
	"""docstring for Post_CreateView"""
	model = Post	
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


def about(request):
    return render(request,'myblog/about.html', {'title': 'About'})