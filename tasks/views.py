from .models import Task
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskCreateSerializer, UserTasksSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from django_filters.rest_framework import DjangoFilterBackend


class TaskCreateAPIView(CreateAPIView):
    serializer_class = TaskCreateSerializer
    queryset = Task.objects.all()


class TaskDetailAPIView(RetrieveAPIView):
    serializer_class = TaskCreateSerializer
    queryset = Task.objects.all()
    lookup_field = 'name'


class TaskEditAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    serializer_class = TaskCreateSerializer
    queryset = Task.objects.all()
    lookup_field = 'name'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TaskListAPIView(ListCreateAPIView):
    serializer_class = TaskCreateSerializer
    queryset = Task.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)


class UserTasks(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        tasks = Task.objects.filter(executor_id=pk)
        serializer = UserTasksSerializer(tasks, many=True)
        return Response(serializer.data)
