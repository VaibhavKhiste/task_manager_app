from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import fetch_external_todos
from .models import Task
from .serializers import TaskSerializer
import requests
from django.db.models import Count


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['GET'])
def task_stats(request):
    return Response({
        "completed": Task.objects.filter(status="COMPLETED").count(),
        "pending": Task.objects.filter(status="PENDING").count(),
    })


@api_view(['GET'])
def weather(request):
    url = "https://api.open-meteo.com/v1/forecast?latitude=18.52&longitude=73.85&current_weather=true"
    response = requests.get(url)
    return Response(response.json())


@api_view(['GET'])
def external_todos(request):
    todos = fetch_external_todos()
    return Response({
        "source": "jsonplaceholder.typicode.com",
        "data": todos
    })


@api_view(['GET'])
def task_report(request):
    total = Task.objects.count()
    completed = Task.objects.filter(status="COMPLETED").count()
    pending = Task.objects.exclude(status="COMPLETED").count()

    return Response({
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending
    })
