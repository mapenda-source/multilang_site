# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot'),
    # Ajoutez d'autres chemins si nécessaire
]
