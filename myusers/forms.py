from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistration(UserCreationForm):

	"""docstring for UserRegistration"""
	email = forms.EmailField() # required=True(default)
	#dob = forms.DateField()


	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		# fields = ['username', 'email', 'dob', 'password1', 'password2']
	

class userupdateform(forms.ModelForm):
	"""docstring for userupdateform"""
	email = forms.EmailField() # required=True(default)

	class Meta:
		model = User
		fields = ['username', 'email']
		# fields = ['username', 'email', 'dob', 'password1', 'password2']
	
class userprofileupdateform(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']