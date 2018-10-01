from django.test import TestCase

# Create your tests here.
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def login(request):
    if request.method == 'GET':
        return redirect('http://132.232.107.63:3000/dashboard')

    return HttpResponse(0)
