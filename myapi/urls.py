from django.urls import path
from .views import *
# These urls patterns are function based
urlpatterns = [
    path('api/comment', comment_list),
    path('edit_delete/<int:pk>/', edit_delete)
]
