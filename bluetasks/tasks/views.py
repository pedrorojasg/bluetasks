from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

from .models import Task
from .serializers import TaskSerializer, CreateTaskSerializer


class TaskViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListCreateViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer
