from django.shortcuts import render
from django.views.generic import DetailView
from .models import Teacher, Student

class TeacherDetailView(DetailView):
    model = Teacher
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.object
        context['courses'] = teacher.courses.all()
        return context

class StudentDetailView(DetailView):
    model = Student
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.object
        context['courses'] = student.courses.all()
        context['teachers'] = Teacher.objects.filter(courses__students=student)
        return context
