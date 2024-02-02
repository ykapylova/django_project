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



@api_view(['POST'])
def update_tasks(request, pk):
	task = Task.objects.get(pk=pk)
	data = TaskSerializer(instance=task, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
@api_view(['DELETE'])
def delete_tasks(request, pk):
	task = get_object_or_404(Task, pk=pk)
	task.delete()
	return Response(status=status.HTTP_202_ACCEPTED)

