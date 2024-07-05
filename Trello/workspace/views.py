from rest_framework import generics
from .models import *
from .serializers import *


class WorkspaceListCreateView(generics.ListCreateAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer


class WorkspaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        workspace_id = self.kwargs['workspace_id']
        return Task.objects.filter(workspace_id=workspace_id)

    def perform_create(self, serializer):
        workspace_id = self.kwargs['workspace_id']
        workspace = Workspace.objects.get(id=workspace_id)
        serializer.save(workspace=workspace)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        workspace_id = self.kwargs['workspace_id']
        task_id = self.kwargs['pk']
        return Task.objects.filter(workspace_id=workspace_id, id=task_id)


class SubTaskListCreateView(generics.ListCreateAPIView):
    serializer_class = SubTaskSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return SubTask.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs['task_id']
        task = Task.objects.get(id=task_id)
        serializer.save(task=task)


class SubTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubTaskSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        subtask_id = self.kwargs['pk']
        return SubTask.objects.filter(task_id=task_id, id=subtask_id)


class UserWorkspaceRoleListCreateView(generics.ListCreateAPIView):
    serializer_class = UserWorkspaceRoleSerializer

    def get_queryset(self):
        workspace_id = self.kwargs['workspace_id']
        return UserWorkspaceRole.objects.filter(workspace_id=workspace_id)

    def perform_create(self, serializer):
        workspace_id = self.kwargs['workspace_id']
        workspace = Workspace.objects.get(id=workspace_id)
        serializer.save(workspace=workspace)


class UserWorkspaceRoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserWorkspaceRoleSerializer

    def get_queryset(self):
        workspace_id = self.kwargs['workspace_id']
        user_id = self.kwargs['user_id']
        return UserWorkspaceRole.objects.filter(workspace_id=workspace_id, user_id=user_id)
