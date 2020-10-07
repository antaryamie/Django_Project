from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'firstapp/home.html')

def login(request):
    return render(request, 'firstapp/login.html')

# def about(request):
#     return HttpResponse("This is the about us page")

# def contact(request):
#     return HttpResponse("This is the contact us")