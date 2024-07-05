from rest_framework import serializers
from .models import *


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


class UserWorkspaceRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkspaceRole
        fields = '__all__'
