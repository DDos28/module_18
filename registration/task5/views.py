from django.shortcuts import render
from .forms import UserRegister

def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f"Приветствуем, {username}!"
        else:
            info['error'] = 'Некорректные данные в форме'

    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)



def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f"Приветствуем, {username}!"
        else:
            info['error'] = 'Некорректные данные в форме'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)