from rest_framework.serializers import ModelSerializer
from .models import Task
from accounts.serializers import UserDetailSerializer

class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'executor',
            'manager'
        ]

class UserTasksSerializer(ModelSerializer):
    manager = UserDetailSerializer(read_only=True)

    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'executor',
            'manager'
        ]
