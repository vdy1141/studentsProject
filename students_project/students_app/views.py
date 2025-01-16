from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("<h1>This is Home Page</h1>")


def about_us(request):
    return HttpResponse("<h1>This is About us Page</h1>")
