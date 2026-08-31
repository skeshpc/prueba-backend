from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Course, Student, StudentCourse
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer, StudentCourseSerializer

# --- ENDPOINTS REST ---
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer

# --- VISTAS HTML ---
def home_view(request):
    return render(request, 'academic/courses.html') # Redirige raíz a Cursos para evitar 404

def courses_view(request):
    return render(request, 'academic/courses.html')

def students_view(request):
    return render(request, 'academic/students.html')