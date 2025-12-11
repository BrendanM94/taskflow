from django.urls import path
from . import views

# URL patterns for task management
urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("signup/", views.signup, name="signup"),
    path("complete/<int:pk>/", views.todo_complete, name="todo_complete"),
    path("edit/<int:pk>/", views.todo_edit, name="todo_edit"),
    path("delete/<int:pk>/", views.todo_delete, name="todo_delete"),
]
