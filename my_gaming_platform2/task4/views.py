from django.shortcuts import render

def index(request):
    context = {'title': 'Главная страница'}
    return render(request, 'fourth_task/index.html', context)

def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'Resident Evil 4']
    context = {'games': games}
    return render(request, 'fourth_task/shop.html', context)

def cart(request):
    games = []
    context = {'games': games}
    return render(request, 'fourth_task/cart.html', context)