from django.shortcuts import render
from django.http import HttpResponse



def loadIndex(request):
    return HttpResponse('<h2>Index Page</h2>')

