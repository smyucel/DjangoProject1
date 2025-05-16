from django.shortcuts import render

from home.models import Question, Setting


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'home'}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'referanslar'}
    return render(request, 'referanslar.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'iletisim'}
    return render(request, 'iletisim.html', context)

def yardim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'yardim'}
    return render(request, 'yardim.html', context)