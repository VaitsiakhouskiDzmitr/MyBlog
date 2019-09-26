from django.shortcuts import render


def hello(request):
    n = 'Dima'
    return render(request, 'blog/index.html', context={'name' : n})

# Create your views here.
