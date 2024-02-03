from django.shortcuts import render
from django.http import HttpResponse

from .models import Task, Category
from rest_framework import permissions, viewsets

from .serializers import TaskSerializer, CategorySerializer

from rest_framework import serializers
from rest_framework import status

from django.shortcuts import get_object_or_404


from rest_framework.decorators import api_view
from rest_framework.response import Response



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

