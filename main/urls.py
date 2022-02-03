from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_text/', views.send_text, name='send_text'),
]