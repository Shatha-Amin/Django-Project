from django.contrib import admin
from .models import Course,Student, Teacher
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'teacher')
    list_filter = ('teacher',)
    search_fields = ('title', 'description')

admin.site.register(Course, CourseAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name',  'email')
    search_fields = ('name', 'email')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)