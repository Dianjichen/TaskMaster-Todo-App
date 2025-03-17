from rest_framework import viewsets
from .models import ToDo
from .serializers import ToDoSerializer
from django.http import JsonResponse

def task_list(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    task_data = [{"title": task.title, "description": task.description, "completed": task.completed} for task in tasks]
    return JsonResponse({"tasks": task_data})
class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
