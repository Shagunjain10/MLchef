from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
	"""docstring for Profile"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='mine.jpg', upload_to='profile_pics')
	def __str__(self):
		return '{} your profile'.format(self.user.username)

	# overwrite the save method
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height>300 or img.width>300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

