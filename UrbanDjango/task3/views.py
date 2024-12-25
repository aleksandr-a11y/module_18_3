from django.shortcuts import render

# Create your views here.
games_list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2']

def func_platform(request):
    return render(request, 'platform.html')

def func_games(request):
    context = {'games': games_list}
    return render(request, 'games.html', context)

def func_cart(request):
    return render(request, 'cart.html')