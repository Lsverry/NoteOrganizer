from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('register/', views.register, name='register'),  
    path('notes/', views.note_list, name='note_list'),  
    path('notes/<int:id>/', views.note_detail, name='note_detail'),  
    path('notes/create/', views.note_create, name='note_create'),  
    path('notes/<int:id>/edit/', views.note_update, name='note_update'),  
    path('notes/<int:id>/delete/', views.note_delete, name='note_delete'),  
]
