# from django.http import httpResponse , HttpResponseRedirect
from django.shortcuts import render , redirect
from .models import Note

def home(request):
    return render(request,home)

def login(request):
    return render(request,login)

def registration(request):
    return render(request,registration)

# def course(request):
#     return render(request,course)

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
        # Add more courses here
    ]

    return render(request,  'course.html', {'courses': courses})

# def course_list(request):
#     course_data = {
#         'title': 'Operating system',
#         'description': '<p>An Operating System(OS) is a software that manages and handles hardware and software resources of a computing device.</p>',
#         'learn_more_url': '#',
        
#         'title': 'Data Communication and Networking',
#         'description': '<p>Transferring data over a transmission medium between two or more devices, systems, or places is known as data communication.</p>',
#         'learn_more_url': '#'

#     }

#     courses = Course.objects.all()
#     return render(request, 'course.html', {'courses': courses} , course_data)

def blog(request):
    return render(request,blog)


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




# def home(request):
#     return render(request,"home.html")

# def login(request):
#     try:
#         if request.method=="post":
#             username=str(request.post.get('username'))
#             password=str(request.post.get('password'))

#             return HttpResponseRedirect ('/home/')
#         except:
#             pass
#     return render(request,"login_page.html")

# def registration(request):
#     try:
#         if request.method=="post":
#             username=str(request.post.get('username'))
#             password=str(request.post.get('password'))
#             conform password=str(request.post.get('password'))
#             email=str(request.post.get('email'))

#              return HttpResponseRedirect ('/home/')
#         except:#             pass
#     return render(request,"registration_page.html")

# def course(request):
#     return render(request,"course.html")

# def blog(request):
#     return render(request,"blog.html")

# def profile(request):
#     return render(request,'profile.html')

# def take_note(request):
#     return render(request,"take_note.html")


