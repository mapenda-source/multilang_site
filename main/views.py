from django.shortcuts import render, redirect
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from .models import Article
from django.conf import settings

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article/article_list.html', {'articles': articles})
    

def change_language(request):
    lang = request.GET.get('lang', settings.LANGUAGE_CODE)
    if lang:
        translation.activate(lang)
        response = redirect('/')
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
        return response
        
    return redirect('/')






