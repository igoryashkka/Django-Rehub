from django.shortcuts import render
from .models import Microcontoller,Category
from .pesmissions import *
from rest_framework import generics, status
from .serializers import HardwareSerializer
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework import viewsets
from rest_framework.decorators import action
from django.forms import model_to_dict
from django.http import Http404

# Create your views here.
def index(request):
    mcu = Microcontoller.objects.all()
    return render(request, 'base_.html', {'mcu':mcu})

class HardwareListAPIView(generics.ListCreateAPIView):
    queryset = Microcontoller.objects.all()
    serializer_class = HardwareSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

class HardwareUpdateAPIView(generics.UpdateAPIView):
    queryset = Microcontoller.objects.all()
    serializer_class = HardwareSerializer
    #permission_classes = [IsOwnerOrReadOnly]

class HardwareDestroyAPI(generics.DestroyAPIView):
    queryset = Microcontoller.objects.all()
    serializer_class = HardwareSerializer
    #permission_classes = [IsAdminOrReadOnly]

class HardwareRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Microcontoller.objects.all()
    serializer_class = HardwareSerializer



