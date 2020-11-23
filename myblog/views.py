from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from myblog.models import Post

def home(request):
	context = {
        'posts': Post.objects.all()
    }
	return render(request,'myblog/home.html',context)


def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	# print(post.title)
	liked = False
	if post.likes.filter(id = request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	
	return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

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
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		current_post = get_object_or_404(Post, id=self.kwargs['pk'])
		liked = False
		if current_post.likes.filter(id=self.request.user.id).exists():
			liked=True

		total_like = current_post.total_like()
		context["total_like"] = total_like
		context["liked"] = liked
		return context

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