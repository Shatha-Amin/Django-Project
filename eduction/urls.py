from django.urls import path
from .views import StudentDetailView

urlpatterns = [
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]