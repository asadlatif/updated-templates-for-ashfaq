from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/', views.profile, name="profile"),
    path('profileEdit/', views.profileEdit, name='profileEdit'),
    path('profile/', views.profile, name='profile'),
    path('instructions/', views.instructions, name='instructions')
]