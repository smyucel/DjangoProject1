from django.shortcuts import render

from .models import Question


def index(request):
    
    text="Django Kurulumu : python -m pip install -e django <br> Proje Oluşturma: django-admin startproject mysite <br> App ekleme: python manage.py startapp.pulls"
    context = {'text': text}
    return render(request, 'index.html', context)