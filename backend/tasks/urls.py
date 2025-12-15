from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, task_stats, weather
from .views import external_todos
from .views import task_report

router = DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/stats/', task_stats),
    path('weather/', weather),
]
urlpatterns += [
    path('external-todos/', external_todos),
]


urlpatterns += [
    path('report/', task_report),
]
