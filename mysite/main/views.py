from django.http import HttpResponse
from django.shortcuts import render

def method(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин одежды Lullaby of Woe',
    }
    return render (request,'main/method.html',context)

def about (request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Крутой сайт бы был,если бы не я делал его))'
    }
    return render (request,'main/about.html',context)
