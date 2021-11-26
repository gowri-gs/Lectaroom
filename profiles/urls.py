from django.urls import path
from .views.home import Index
from .views.user_reg_log import TeacherRegister, StudentRegister,LoginView,LogoutView
from .views.teacher import TeacherDashboard
from .views.student import StudentDashboard

urlpatterns = [

    path('', Index.as_view(), name='index'),
    path('signup/',TeacherRegister.as_view(),name='signup'),
    path('76543210987654321/',StudentRegister.as_view(),name='student_register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('teacher/',TeacherDashboard.as_view(),name='teacher'),
    path('student/',StudentDashboard.as_view(),name='student'),

] 