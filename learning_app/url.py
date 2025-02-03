from django.urls import path ,include
from . import views


from django.contrib import admin
from learning_app import views

# urlpatterns = [
#     # path('admin/', admin.site.urls), 
#     path('',views.home , name='home'),
#     path('about/',views.about , name='about'),
#     path('login/',views.login , name='login'),
#     path('registration/',views.registration , name='registration '),
#     path('course/',views.course , name='course'),
#     path('blog/',views.blog , name='blog'),
#     path('profile/',views.profile , name='profile'),
#     path('take_note/',views.take_note , name='take_note'),
# ]

# urlpatterns = [
     
#     path('',views.home),
#     path('login/',views.login),
#     path('registration/',views.registration),
#     path('course/',views.course),
#     path('blog/',views.blog),
#     path('take_note/',views.take_note),

# ]



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

    # path('',views.home , name='home'),
    # path('about/',views.about , name='about'),
    # path('login/',views.login , name='login'),
    # path('registration/',views.registration , name='registration'),
    # path('course/',views.course , name='course'),
    # path('blog/',views.blog , name='blog'),
    # path('profile/',views.profile , name='profile'),
    # path('take_note/',views.take_note , name='take_note'),
]
