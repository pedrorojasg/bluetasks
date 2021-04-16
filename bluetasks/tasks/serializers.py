from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('created', )


class CreateTaskSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        task = Task.objects.create(**validated_data)
        return task

    class Meta:
        model = Task
        fields = (
            'title', 'type', 'status', 'priority', 'description',
            'created_by', 'project', 'epic',
            'tags', 'comments', 'owners', 'linked_tasks',
        )
        extra_kwargs = {}
