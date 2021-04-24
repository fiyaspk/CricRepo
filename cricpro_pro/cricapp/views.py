from django.shortcuts import render
from django.http import HttpResponse
def TestFn(request):
    return HttpResponse('heloo')
def html1(request):
    return render(request,'design.html')

# Create your views here.
