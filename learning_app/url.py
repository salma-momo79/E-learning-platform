from django.urls import path ,include
from . import views
from django.contrib import admin
from learning_app import views

urlpatterns = [

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('courses/', course_list, name='course'),
    path('blog/', blog, name='blog'),
    path('profile/', profile, name='profile'),
    path('take_note/', take_note, name='take_note'),
    path('saved-notes/', saved_notes, name='saved_notes'),

]
