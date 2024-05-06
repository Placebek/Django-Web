from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'hokken/index.html')

def about(request):
  return HttpResponse("<p>About us</p>")
  