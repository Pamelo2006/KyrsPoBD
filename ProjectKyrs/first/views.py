from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm, CardForm
from .models import Users, Orders, UserCreditCart
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def useracount(request):
    orders = Orders.objects.all()
    return render(request, 'useracount.html', {'orders': orders})

def index(request):
    return render(request, "index.html")

def brends(request):
    return render(request, "brends.html")

def post_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = Users(
                user_name=form.cleaned_data['user_name'],
                login=form.cleaned_data['login'],
                password=form.cleaned_data['password']
            )
            user.save()
            return redirect('useracount')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def handle_user_actions(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Login':
            form = LoginForm(request.POST)
            if form.is_valid():
                login = form.cleaned_data['login']
                password = form.cleaned_data['password']
                user = authenticate(request, login=login, password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'useracount.html', {'username': user.user_name, 'action': 'logged in'})
                else:
                    return render(request, 'useracount.html', {'error': 'Invalid login or password.'})
            else:
                return render(request, 'useracount.html', {'form': form})
    return render(request, 'useracount.html')


def user_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = UserCreditCart(
                nomer=form.cleaned_data['nomer'],
                cvcode=form.cleaned_data['cvcode']
            )
            card.save()
            return redirect('useracount')
    else:
        form = CardForm()
    return render(request, 'create_user.html', {'form': form})