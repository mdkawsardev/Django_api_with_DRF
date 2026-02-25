from django.urls import path
from .views import *
# These urls patterns are class based
urlpatterns = [
    path('student_data/', Student_List.as_view()),
    path('student_data/<int:pk>', Edit_Students.as_view())
]
