from rest_framework import serializers
from task.models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # tasks = TaskSerializer(many=True)
    #
    # def create(self, validated_data):
    #     tasks_data = validated_data.pop("tasks")
    #     user = User.objects.create(**validated_data)
    #     for task_data in tasks_data:
    #         Task.objects.create(user=user, task=task_data)
    #     return user

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'tasks')
