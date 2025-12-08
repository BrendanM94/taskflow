from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo


@login_required
def todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")

        if title:
            Todo.objects.create(
                user=request.user,
                title=title,
                description=description
            )

        return redirect("todo_list")

    todos = Todo.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "todo/todo_list.html", {"todos": todos})


def todo_complete(request, pk):
    return redirect("todo_list")


def todo_delete(request, pk):
    return redirect("todo_list")


def todo_edit(request, pk):
    return redirect("todo_list")


def signup(request):
    return redirect("login")
