from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Course 
from .models import Note
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

def course_list(request):
    courses = [
        {
            'title': 'Operating System',
            'description': 'This is a software that manages and handles hardware and software resources of a computing device.',
            'learn_more_url': '#'
        },
        {
            'title': 'Data Communication and Networking',
            'description': 'This course benefits are transferring data over a transmission medium between two or more devices, systems, or places is known as data communication.',
            'learn_more_url': '#'
        },
        # Add more courses here
    ]

    return render(request,  'course.html', {'courses': courses})



def blog(request):
    return render(request, 'blog.html')

def profile(request):
    return render(request, 'profile.html')


# def take_note(request):
#     return render(request, 'take_note.html')

# view for take note feature

# from django.shortcuts import render, redirect
# from .models import Note  # Ensure this import is present

def take_note(request):
    if request.method == 'POST':
        title = request.POST.get('note-title')
        content = request.POST.get('note-content')
        Note.objects.create(title=title, content=content)
        return redirect('saved_notes')  # Redirect to the saved notes page
    return render(request, 'take_note.html')

def saved_notes(request):
    notes = Note.objects.all().order_by('-created_at')  # Fetch all notes, newest first
    return render(request, 'saved_notes.html', {'notes': notes})
