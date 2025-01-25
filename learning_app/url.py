from django.urls import path ,include
from . import views


from django.contrib import admin
from learning_app import views

urlpatterns = [
     
    path('',views.home),
    path('login/',views.login),
    path('registration/',views.registration),
    path('course/',views.course),
    path('blog/',views.blog),
    path('take_note/',views.take_note),

]

# urlpatterns = [

#     path('',views.home , name='home'),
#     path('login/',views.login , name='login'),
#     path('registration/',views.registration , name='registration '),
#     path('course/',views.course , name='course'),
#     path('blog/',views.blog , name='blog'),
#     path('take_note/',views.take_note , name='take_note'),
# ]
