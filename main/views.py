from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
#    return HttpResponse('Home page')

def index(request):
    context={
        'title' : 'Home - Главная',
        'content' : 'Магазин мебели HOME'
    }
    return render(request, 'main/about.html', context)


def about(request):
    context={
        'title' : 'Home - О нас',
        'content' : 'О нас',
        'text_on_page' : 'Текст большой текст. Текст большой текст. Текст большой текст. Текст большой текст. Текст большой текст. Текст большой текст. Текст большой текст. Текст большой текст.'
    }
    return render(request, 'main/about.html', context)