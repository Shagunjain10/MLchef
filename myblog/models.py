from django.db import models
from django.urls import reverse
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='post_like')

    def __str__(self):
        return self.title

    def total_like(self):
        return self.likes.count()

    def get_absolute_url(self):
    	# this function return the string contain url on which have to redirect
    	return reverse('post-detail', kwargs={'pk': self.pk})

# Comment Section
class Comment(models.Model):
    serial_no= models.AutoField(primary_key=True)
    comment_text=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=timezone.now)

