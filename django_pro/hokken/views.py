from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  for i in range(10):
    return HttpResponse("<h4>Проверка работы<h4>")
  