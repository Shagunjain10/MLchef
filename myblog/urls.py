from django.urls import path
from . import views
from .views import (
	Post_ListView, 
	Post_DetailView, 
	Post_CreateView,
	Post_DeleteView,
	userPost_ListView
)

urlpatterns = [
    #path('', views.home, name='blog-home'), 
    path('', Post_ListView.as_view(), name='blog-home'),
    path('user/<str:username>/', userPost_ListView.as_view(), name='blog-user_post'),
    path('post/<int:pk>/', Post_DetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', Post_DeleteView.as_view(), name='post-delete'), # model_confirm_delete
    path('post/create/', Post_CreateView.as_view(), name='post-create'), # template is 'model_form.html'
    path('about/', views.about, name='blog-about'),
]