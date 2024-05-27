from django.contrib import admin
from django.urls import path, include
from notes import views as notes_views
from django.contrib.auth import views as auth_views

# Define the URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),  
    path('register/', notes_views.register, name='register'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]