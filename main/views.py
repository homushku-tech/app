from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Главная страница Серафим ',
        'list': ['first','second'],
        'is_authenticated': False
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('Homepage')
