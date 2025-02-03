from django.shortcuts import render , redirect
from .models import Note

def home(request):
    return render(request,home)

def login(request):
    return render(request,login)

def registration(request):
    return render(request,registration)

def course_list(request):
    courses = [
        {
            'title': 'Operating System',
            'description': 'This is a software that manages and handles hardware and software resources of a computing device.,
            'learn_more_url': '#'
        },
        {
            'title': 'Data Communication and Networking',
            'description': 'This course benefits are transferring data over a transmission medium between two or more devices, systems, or places is known as data communication.',
            'learn_more_url': '#'
        },

    ]

    return render(request,  'course.html', {'courses': courses})

def blog(request):
    return render(request,blog)


def take_note(request):
    if request.method == 'POST':
        title = request.POST.get('note-title')
        content = request.POST.get('note-content')
        Note.objects.create(title=title, content=content)
        return redirect('saved_notes')  
    return render(request, 'take_note.html')

def saved_notes(request):
    notes = Note.objects.all().order_by('-created_at')  
    return render(request, 'saved_notes.html', {'notes': notes})
