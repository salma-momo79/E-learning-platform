from django.contrib import admin
from .models import Course
from .models import Note


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     search_fields = ('title',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Ensure created_at is correct
