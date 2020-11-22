"""myblogsite URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from myusers import views as myusers_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myblog.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='myusers/login.html'), name='login'), # default goes to registration/login.html
    path('logout/', auth_views.LogoutView.as_view(template_name='myusers/logout.html'), name='logout'),
    path('register/', myusers_views.register, name='register'),
    path('profile/', myusers_views.profile, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
