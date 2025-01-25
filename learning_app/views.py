from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# from django.http import httpResponse

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login_page.html')

def registration(request):
    return render(request,'registration_page.html')

def course(request):
    return render(request,'course.html')

def blog(request):
    return render(request,'blog.html')

def take_note(request):
    return render(request,'take_note.html')


