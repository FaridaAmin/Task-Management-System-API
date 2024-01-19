from django.shortcuts import render
from rest_framework import generics
from .models import TMSys
from .serializer import TasksSerializer

# Create your views here.
class TaskListCreate(generics.ListCreateAPIView):
    queryset=TMSys.objects.all()
    serializer_class= TasksSerializer

class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = TMSys.objects.all()
    serializer_class=TasksSerializer


