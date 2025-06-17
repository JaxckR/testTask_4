from django.shortcuts import render

from menu.models import Category


def index(request):
    return render(request, 'menu/index.html')


def show_all_menu(request):
    menu = list(Category.objects.filter(level=0))

    return render(request, 'menu/show_all_menu.html', {
        'menu': menu,
    })


def show_path(request, path):
    return render(request, 'menu/show_path.html', {
        'path': path,
    })
