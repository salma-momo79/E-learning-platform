from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# from django.http import httpResponse

def home(request):
    return render(request, 'home.html')

# def login(request):
#     try:
#         if request.method=="post":
#             username=str(request.post.get('username'))
#             password=str(request.post.get('password'))

#             return HttpResponseRedirect ('/home/')
#         else:
#             pass
#     return render(request,'login_page.html')

# def registration(request):
#     try:
#         if request.method=="post":
#             username=str(request.post.get('username'))
#             password=str(request.post.get('password'))
#             conform password=str(request.post.get('password'))
#             email=str(request.post.get('email'))

#              return HttpResponseRedirect ('/home/')
#         else:
#             pass
#     return render(request,'registration_page.html')


def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login_page.html')

def registration(request):
    return render(request, 'registration_page.html')

def course(request):
    return render(request, 'course.html')

def blog(request):
    return render(request, 'blog.html')

def profile(request):
    return render(request, 'profile.html')


def take_note(request):
    return render(request, 'take_note.html')


