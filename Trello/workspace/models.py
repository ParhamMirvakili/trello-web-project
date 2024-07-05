from django.db import models
from authentication.models import User


class Workspace(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(name=''), name='name_not_empty')
        ]

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    estimated_time = models.FloatField(blank=True, null=True)
    actual_time = models.DurationField(blank=True, null=True)
    due_date = models.DurationField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, blank=True, null=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(title=''), name='task_title_not_empty'),
            models.CheckConstraint(check=~models.Q(workspace_id=''), name='task_workspace_not_empty')
        ]

    def __str__(self):
        return self.title


class SubTask(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(title=''), name='subtask_title_not_empty'),
            models.CheckConstraint(check=~models.Q(task_id=''), name='task_not_empty')
        ]

    def __str__(self):
        return self.title


class UserWorkspaceRole(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Standard', 'Standard'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey('Workspace', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(user_id=''), name='user_not_empty'),
            models.CheckConstraint(check=~models.Q(workspace_id=''), name='role_workspace_not_empty')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.role} in {self.workspace.name}"
git add .