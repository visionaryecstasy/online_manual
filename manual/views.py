from django.shortcuts import render

from .import models
from datetime import time
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def python_data_chapter1(request):
    chapter1 = models.Manual.objects.filter(category='chapter1')
    return render(request, "manual_chapter/chapter1.html", {'chapter1':chapter1})

def python_data_chapter2(request):
    chapter2 = models.Manual.objects.filter(category='chapter2')
    return render(request, "manual_chapter/chapter2.html", {'chapter2':chapter2})

def python_data_chapter3(request):
    chapter3 = models.Manual.objects.filter(category='chapter3')
    return render(request, "manual_chapter/chapter3.html", {'chapter3':chapter3})

def notification_board(request):
    message = models.Message.objects.all()
    return render(request, 'manual_chapter/notification_board.html', {'message': message})

def manual(request):
    return render(request,'index.html')