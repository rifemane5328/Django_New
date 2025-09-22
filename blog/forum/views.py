from django.shortcuts import render
from django.http import HttpResponse

def home(request1):
    return HttpResponse('Hello World')


def test(request2):
    return render(request2, 'forum/index.html')
