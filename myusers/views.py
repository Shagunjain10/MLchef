from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm 
# this form will handle all related user registration
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistration, userupdateform, userprofileupdateform
# Create your views here.

def register(request):
	if request.method=='POST':
		form = UserRegistration(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,'Your account created {}. Please Login'.format(username))
			return redirect('login')
	else:
		form = UserRegistration()
	return render(request, 'myusers/register.html',{'form':form})

@login_required
def profile(request):
	if request.method=='POST':
		uform = userupdateform(request.POST, instance=request.user)
		pform = userprofileupdateform(request.POST, request.FILES, instance=request.user.profile)
		if uform.is_valid and pform.is_valid:
			uform.save()
			pform.save()
			username = uform.cleaned_data.get('username')
			messages.success(request,'Your profile updated {} !!.'.format(username))
			return redirect('profile')
	else:
		uform = userupdateform(request.POST, instance=request.user)
		pform = userprofileupdateform(request.POST, request.FILES, instance=request.user.profile)
	context = {
	'uform': uform,
	'pform': pform
	}


	return render(request, 'myusers/profile.html', context)
# 