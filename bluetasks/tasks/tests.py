import os
import pdb

from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Project, Epic, Task


class TaskTests(APITestCase):
    """
    Unit tests to validate Task model, urls and views.
    """
    # Revisar lo de force_auth ejemplos
    # Add setup
    # Test de custom login
    list_create_url = reverse('task-list')
    user_dict = {"email": "hola@example.com", "password": "c1rb0xl1fe"}

    def setUp(self):
        (user, _non_use) = get_user_model().objects.get_or_create(**self.user_dict)
        self.my_user = user

    def test_create_basic_task_in_db(self):
        """
        Ensure we can create (POST) a Task.
        """
        project = Project.objects.create(title="Project1")
        epic = Epic.objects.create(title="Epic1")
        user = get_user_model().objects.create(username="tester1")

        data = {
            'title': "Task test",
            'type': 1,
            'status': 1,
            'priority': 1,
            'description': "A simple task.",
            'project': project.id,
            'epic': epic.id,
            'created_by': user.id,
        }

        self.client.force_authenticate(self.my_user)
        response = self.client.post(self.list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_list_tasks(self):
        """
        Ensure we can list (GET) tasks.
        """
        project = Project.objects.create(title="Project1")
        epic = Epic.objects.create(title="Epic1")
        user = get_user_model().objects.create(username="tester1")

        data = {
            'title': "Task test",
            'type': 1,
            'status': 1,
            'priority': 1,
            'description': "A simple task.",
            'project': project,
            'epic': epic,
            'created_by': user,
        }
        Task.objects.create(**data)
        Task.objects.create(**data)

        self.client.force_authenticate(self.my_user)
        response = self.client.get(self.list_create_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(len(response.json()['results']), 2)

