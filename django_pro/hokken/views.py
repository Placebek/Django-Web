from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  data = {
    'title': 'Главная страница',
    'values': ['set', '10', '10-12-2024']
  }
  return render(request, 'hokken/index.html', data)

def about(request):
  return render(request, 'hokken/about.html')

  