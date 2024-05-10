from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  data = {
    'title': 'Главная страница'
  }
  return render(request, 'hokken/index.html', data)

def about(request):
  return render(request, 'hokken/about.html')
  