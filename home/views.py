from django.shortcuts import render

from home.models import Question, Setting


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'index.html', context)
