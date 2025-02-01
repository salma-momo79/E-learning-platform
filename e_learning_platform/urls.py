"""
URL configuration for e_learning_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from learning_app import views

# urlpatterns = [
#     path('admin/', admin.site.urls), 
#     path('', home, name='home'),
#     path('about/', about, name='about'),
#     path('login/', login, name='login'),
#     path('registration/', registration, name='registration'),
#     path('course/', course, name='course'),
#     path('blog/', blog, name='blog'),
#     path('profile/', profile, name='profile'),
#     path('take_note/', take_note, name='take_note'),

# ]
# urlpatterns = [
#     path('admin/', admin.site.urls), 
#     path('',views.home),
#     path('login/',views.login),
#     path('registration/',views.registration),
#     path('course/',views.course),
#     path('blog/',views.blog),
#     path('profile/',views.profile),
#     path('take_note/',views.take_note),

# ]

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',views.home , name='home'),
    path('login/',views.login , name='login'),
    path('registration/',views.registration , name='registration'),
    path('about/',views.about , name='about'),
    path('course/',views.course , name='course'),
    path('blog/',views.blog , name='blog'),
    path('profile/',views.profile , name='profile'),
    path('take_note/',views.take_note , name='take_note'),
]