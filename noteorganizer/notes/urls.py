from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('<int:id>/', views.note_detail, name='note_detail'),
    path('create/', views.note_create, name='note_create'),
    path('<int:id>/edit/', views.note_update, name='note_update'),
    path('<int:id>/delete/', views.note_delete, name='note_delete'),
]