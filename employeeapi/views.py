from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def taskList(request):
    tasks= Task.objects.all()
    serializer= TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()
        return Response("Added Successfully")
    return Response("Failed to Add")  


