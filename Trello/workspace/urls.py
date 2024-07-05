from django.urls import path
from .views import *

urlpatterns = [
    # Workspace URLs
    path('workspaces/', WorkspaceListCreateView.as_view(), name='workspace-list-create'),
    path('workspaces/<int:pk>/', WorkspaceDetailView.as_view(), name='workspace-detail'),

    # Task URLs
    path('workspaces/<int:workspace_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('workspaces/<int:workspace_id>/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    # SubTask URLs
    path('tasks/<int:task_id>/subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('tasks/<int:task_id>/subtasks/<int:pk>/', SubTaskDetailView.as_view(), name='subtask-detail'),

    # UserWorkspaceRole URLs
    path('workspaces/<int:workspace_id>/users/', UserWorkspaceRoleListCreateView.as_view(),
         name='user-workspace-role-list-create'),
    path('workspaces/<int:workspace_id>/users/<int:user_id>/', UserWorkspaceRoleDetailView.as_view(),
         name='user-workspace-role-detail'),
]
