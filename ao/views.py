from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'ao/home.html')

def reservation(request):
    return render(request, 'ao/reservation.html')