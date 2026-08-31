from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from academic import views

router = DefaultRouter()
router.register(r'teachers', views.TeacherViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'student-courses', views.StudentCourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # Enmascaramiento de vistas HTML
    path('', views.home_view, name='home'),
    path('courses/', views.courses_view, name='courses_page'),
    path('students/', views.students_view, name='students_page'),
]