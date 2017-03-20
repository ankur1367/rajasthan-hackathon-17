from django.shortcuts import render
from rest_framework import viewsets
from .models import Scheme
from .serializers import SchemeSerializer
# Create your views here.

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer
