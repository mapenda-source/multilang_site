from django.contrib import admin
from django.urls import include, path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),
      path('', include('main.urls')),
    path('change-language/', views.change_language, name='change_language'),
   
  
]


