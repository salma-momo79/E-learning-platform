from django.contrib import admin
from .models import Course
from .models import Note

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  
