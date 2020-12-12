from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list', views.tasklist, name="Task-list"),
    path('task-Detail/<str:pk>/', views.taskDetail, name="Task-Detail"),
]
